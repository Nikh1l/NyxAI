from pathlib import Path

def capability_banner(capability, action, target):

    print()
    print("=" * 60)
    print(f"Capability : {capability}")
    print(f"Action     : {action}")
    print(f"Target     : {Path(target)}")
    print("=" * 60)
    print()