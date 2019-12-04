import Y18.Tests as Year18
import Y19.Tests as Year19

if __name__ == "__main__":
    print("\u2554" + "\u2550" * 32 + "\u2557")
    print("\u2551" + "\u2550" * 8 + " Advent of Code " + "\u2550" * 8 + "\u2551")
    default = True if input("\u2551 Use default filesystem [y/n]?  \u2560\u2550 ") in ('y', 'Y') else False
    Year19.testing(default)
    # Year18.testing(default)