def get_pi_digits(n):
    """
    Returns the first n digits of Pi.
    Note: For a large number of digits, consider using a file or an API.
    """
    pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    return pi[:n+2]  # +2 to account for '3.'


def chunk_pi(digits, chunk_size=4):
    """
    Breaks down the Pi digits into smaller chunks for easier memorization.
    """
    chunks = [digits[i:i+chunk_size] for i in range(2, len(digits), chunk_size)]
    return ' '.join(chunks)


def generate_song_piem(digits):
    # Example mapping of digits to song lyrics
    lyrics_by_length = [
        "", "I", "we", "you", "love", "never", "always", "forever", "together", "remember",  # 0-9 letters
        # Add more lyrics for larger digits if needed
    ]

    piem = []
    for digit in digits:
        if digit == '.':
            piem.append('point')  # Word for the decimal point
        else:
            word_length = int(digit)
            piem.append(lyrics_by_length[word_length])

    return ' '.join(piem)


def pi_game():
    level = 1
    while True:
        pi_digits_to_level = get_pi_digits(level + 3)  # Get the next 3 digits
        next_three_digits = pi_digits_to_level[-3:]  # Isolate the next three digits
        song_piem_for_next_three = generate_song_piem(next_three_digits)  # Generate song piem for these digits
        print(f"\nLevel {level}: Pi up to this point: {pi_digits_to_level[:-3]}")
        print(f"Next Digits Guide: {next_three_digits}")
        print(f"Song Piem for Next Digits: {song_piem_for_next_three}")
        user_input = input("Enter the next 3 digits of Pi: ")

        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        if user_input == next_three_digits:
            level += 3  # Increase level by 3 as 3 digits are entered each time
        else:
            print(f"Try again. The correct digits were {next_three_digits}")
            # Do not break; let the user continue or choose to exit

    print(f"Game Over! You reached level {level}")

if __name__ == "__main__":
    pi_game()