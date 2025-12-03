#!/bin/python

from collections import Counter

class SecurityLog:
    def __init__(self, metadata):
        self._entries = []
        self._metadata = metadata

    def add_entry(self, text):
        self._entries.append(text)

    def get_entries(self):
        return tuple(self._entries)

    def analyze(self):
        return len(self._entries)


class FirewallLog(SecurityLog):
    def analyze(self):
        deny_entries = [entry for entry in self._entries if "DENY" in entry]
        ips = []
        for entry in deny_entries:
            parts = entry.split()
            if len(parts) >= 2:
                ips.append(parts[1])
        
        ip_counts = Counter(ips)
        
        return {
            "blocked_packets": len(deny_entries),
            "top_3_ips": ip_counts.most_common(3)
        }


class AuthLog(SecurityLog):
    def analyze(self):
        failed_entries = [entry for entry in self._entries if "FAILED" in entry]
        users = []
        for entry in failed_entries:
            parts = entry.split()
            if len(parts) >= 3:
                users.append(parts[2])
        
        user_counts = Counter(users)
        
        return {
            "failed_logins": len(failed_entries),
            "top_3_accounts": user_counts.most_common(3)
        }


class IDSLog(SecurityLog):
    def analyze(self):
        signatures = ["SQL_INJECTION", "XSS", "PORT_SCAN"]
        found_signatures = []
        
        for entry in self._entries:
            for signature in signatures:
                if signature in entry:
                    found_signatures.append(signature)
        
        sig_counts = Counter(found_signatures)
        most_common = sig_counts.most_common(1)
        
        return {
            "all_found": found_signatures,
            "unique_signatures": set(found_signatures),
            "most_frequent": most_common[0] if most_common else None
        }


if __name__ == "__main__":
    firewall = FirewallLog(("firewall", "HIGH", 1))
    auth = AuthLog(("auth_service", "CRITICAL", 2))
    ids = IDSLog(("ids_system", "MEDIUM", 3))

    firewall.add_entry("2023-10-27 192.168.1.10 DENY Blocked connection")
    firewall.add_entry("2023-10-27 10.0.0.5 ALLOW Connection established")
    firewall.add_entry("2023-10-27 192.168.1.10 DENY Blocked connection")
    firewall.add_entry("2023-10-27 172.16.0.1 DENY Blocked connection")
    firewall.add_entry("2023-10-27 192.168.1.10 DENY Blocked connection")
    firewall.add_entry("2023-10-27 172.16.0.1 DENY Blocked connection")

    auth.add_entry("2023-10-27 SESSION root FAILED Wrong password")
    auth.add_entry("2023-10-27 SESSION admin SUCCESS Logged in")
    auth.add_entry("2023-10-27 SESSION root FAILED Wrong password")
    auth.add_entry("2023-10-27 SESSION guest FAILED Account locked")
    auth.add_entry("2023-10-27 SESSION user1 FAILED Wrong password")
    auth.add_entry("2023-10-27 SESSION root FAILED Wrong password")

    ids.add_entry("Warning: Detect SQL_INJECTION attempt in query")
    ids.add_entry("Info: Normal traffic flow")
    ids.add_entry("Alert: XSS payload detected in header")
    ids.add_entry("Warning: Detect SQL_INJECTION attempt in query")
    ids.add_entry("Critical: PORT_SCAN detected from external IP")
    ids.add_entry("Warning: Detect SQL_INJECTION attempt in query")

    logs_system = [firewall, auth, ids]

    for log_object in logs_system:
        result = log_object.analyze()
        print(f"Wynik analizy dla {type(log_object).__name__}: {result}")