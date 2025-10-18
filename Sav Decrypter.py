import re
import struct

def guess_numbers(byte_seq):
    """Try to guess nearby numeric values (ints/floats) from byte sequence."""
    nums = []
    # Read in 4-byte chunks
    for i in range(0, len(byte_seq) - 3, 4):
        chunk = byte_seq[i:i+4]
        try:
            i_val = struct.unpack("<I", chunk)[0]
            f_val = struct.unpack("<f", chunk)[0]
            # Filter out unrealistic values
            if 0 < i_val < 1_000_000_000:
                nums.append(f"int={i_val}")
            if 0.001 < abs(f_val) < 1e5:
                nums.append(f"float={f_val:.3f}")
        except:
            pass
    return ", ".join(nums) if nums else "no clear numbers"

def analyze_sav(file_path, output_file="game_analysis.txt", min_length=3, context=16):
    with open(file_path, "rb") as f:
        data = f.read()

    matches = list(re.finditer(rb"[ -~]{%d,}" % min_length, data))
    lines = []
    lines.append("=== Charlie Murder .SAV Analysis ===\n")  # Chaneg to your game nnme

    for m in matches:
        start = max(0, m.start() - context)
        end = min(len(data), m.end() + context)
        before = data[start:m.start()]
        after = data[m.end():end]

        guessed = guess_numbers(after[:16])  # try to read possible numbers after string

        lines.append(f"Offset 0x{m.start():06X}:")
        lines.append(f"  String: {m.group().decode(errors='ignore')}")
        lines.append(f"  Before Bytes: {before.hex(' ')}")
        lines.append(f"  After Bytes : {after.hex(' ')}")
        lines.append(f"  Guess: {guessed}")
        lines.append("-" * 60 + "\n")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))

    print(f"✅ Analysis complete! Saved to: {output_file}")
    print(f"📄 Total strings found: {len(matches)}")


if __name__ == "__main__":
    analyze_sav("game.sav") # Chaneg to your game file

