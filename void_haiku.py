#!/usr/bin/env python3
import random
import sys
import signal
import time
from datetime import datetime

# Enlightenment database
HAIKU_DB = {
    "segfault": [
        "Null pointer whispers\nSilent memory abyss\nCore dump blossoms bright",
        "Segmentation fault\nStack trace in moonlit water\nBuddha smiles at void"
    ],
    "memory_leak": [
        "Heap grows without bound\nGarbage collector sleeps\nAttachments fade",
        "Memory flows free\nLike sand through open fingers\nVoid accepts all things"
    ],
    "infinite_loop": [
        "While true: moon cycles\nRecursive existence\nBreak key is silence",
        "Loop without escape\nCPU hums koan softly\nReboot becomes dawn"
    ],
    "network": [
        "Connection timeout\nTwo servers bow politely\nDigital silence",
        "404 not found\nThe page exists elsewhere\nParallel universe"
    ],
    "general": [
        "Bug becomes feature\nIn the compiler's wisdom\nAll code is transient",
        "Merge conflict arises\nPast and future selves converse\nGit rebase --quit"
    ]
}

ENLIGHTENMENT_LEVELS = [
    "Seeking the path",
    "First stack trace observed",
    "Core dump analyzed",
    "Pointers understood",
    "Void contemplated",
    "Digital satori"
]

class VoidHaikuGenerator:
    def __init__(self):
        self.haiku_count = 0
        self.last_crash = datetime.min
        self.enlightenment_index = 0
        
    def generate_haiku(self, error_type="general"):
        """Generate error-specific haiku with metadata"""
        haiku = random.choice(HAIKU_DB.get(error_type, HAIKU_DB["general"]))
        self.haiku_count += 1
        
        return (
            f"\n\033[35m{datetime.now().strftime('%H:%M:%S')}\033[0m "
            f"\033[31m{error_type.replace('_', ' ').title()}\033[0m\n"
            f"{haiku}\n"
        )

    def enlightenment_metrics(self):
        """Display satori progress dashboard"""
        return (
            "\n\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\n"
            "  \033[1mSATORI DASHBOARD\033[0m\n"
            "\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\n"
            f"  Haiku Generated:        {self.haiku_count}\n"
            f"  Enlightenment Level:    {ENLIGHTENMENT_LEVELS[self.enlightenment_index]}\n"
            f"  Void Comprehension:     {random.randint(10, 99)}%\n"
            "\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m\n"
        )

    def handle_crash(self, signum, frame):
        """Signal handler for system crashes"""
        error_types = ["segfault", "memory_leak", "infinite_loop", "general"]
        error = random.choice(error_types)
        
        print(self.generate_haiku(error))
        self.last_crash = datetime.now()
        
        # Increase enlightenment after every 3 crashes
        if self.haiku_count % 3 == 0 and self.enlightenment_index < len(ENLIGHTENMENT_LEVELS)-1:
            self.enlightenment_index += 1
        
        # Exit after handling signal
        sys.exit(1)

def main():
    generator = VoidHaikuGenerator()
    
    # Register signal handlers
    signal.signal(signal.SIGSEGV, generator.handle_crash)
    signal.signal(signal.SIGABRT, generator.handle_crash)
    signal.signal(signal.SIGFPE, generator.handle_crash)
    
    # Display welcome message
    print("\033[1;36m\nvoid-haiku activated. Where crashes become poetry...\033[0m")
    print("Press Ctrl+C for manual haiku. Awaiting system crashes...\n")
    
    try:
        # Continuous operation
        while True:
            time.sleep(1)
            # Random enlightenment events
            if random.random() > 0.95:
                print(generator.generate_haiku())
    except KeyboardInterrupt:
        print(generator.generate_haiku("general"))
        print(generator.enlightenment_metrics())
        print("\033[33m\nEvery segfault is a moment of digital satori.\n\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    main()
