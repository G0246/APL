# Ghost leg game
# Last updated: 14/12/24

# Visualize the diagram
def print_amida(amida, players):
    # Calculate the width for player numbers and row numbers
    player_width = len(str(players)) + 2
    row_width = len(str(len(amida))) + 2

    # Header
    header = " " * row_width
    for player in range(1, players + 1):
        header += f"P{player:<{player_width - 1}}"
    print(header)

    # Rows and columns
    for row in range(len(amida)):
        row_str = f"{row + 1:>{row_width}}"
        for col in range(len(amida[row])):
            if amida[row][col]:
                row_str += "|" + "-" * (player_width - 1)
            else:
                row_str += "|" + " " * (player_width - 1)
        row_str += "|"
        print(row_str)

    # Result header
    result_header = " " * row_width
    for result in range(1, players + 1):
        result_header += f"A{result:<{player_width - 1}}"
    print(result_header)

    print()

# BETA (Working as 14/12/24)
# Path simulation
def simulate_paths(amida, players):
    results = {}

    for player in range(players):
        current_col = player
        for row in range(len(amida)):
            if current_col < len(amida[row]) and amida[row][current_col]:
                # Move right
                current_col += 1
            elif current_col > 0 and amida[row][current_col - 1]:
                # Move left
                current_col -= 1
        results[player] = current_col
    return results

# Main function (This is killing me)
def main():
    print("Welcome to the Ghost Leg Game (Amida)!")


    # Ask the user
    try:
        players = int(input("Enter the number of columnns (players): "))
        rows = int(input("Enter the number of rows: "))
        # min_lines = int(input("Enter the minimum number of lines to add (at least 5): "))
    except ValueError:
        print("Invalid input. Please enter only integers!")
        return

    amida = []

    # Setup the array
    for row_index in range(rows):
        row = []
        for col_index in range(players - 1):
            row.append(False)

        amida.append(row)

    print("\nInitial Amida Diagram:")
    print_amida(amida, players)
    # print(f"\nYou need to add at least {min_lines} lines.")

    lines_added = 0
    want_to_exit = False

    while lines_added < rows:
        try:
            print("Current round: ", lines_added)
            row = int(input(f"Enter the row (1 to {rows}) to add a line: ")) - 1
            col = int(input(f"Enter the column (1 to {players - 1}) to add a line: ")) - 1
            
            if not (0 <= row < rows and 0 <= col < players - 1):
                print("Invalid row or column. Try again.")
                continue
            
            # BROKEN
            # Check if there is a line in the left or right column of the same row
            if (col > 0 and amida[row][col - 1]) or (col < players and amida[row][col]):
                print("A line already exists in the adjacent columns. Try a different column.")
                continue

            amida[row][col] = True
            lines_added += 1

            print(f"\nAmida Diagram after adding line at row {row + 1}, column {col + 1}:")
            print_amida(amida, players)
        except ValueError:
            stop  = input("""Invalid input, press enter again if you want to try again. \nOr perhaps you want to exit? Type "q" to exit: """)
            if stop == "q" or "exit":
                break

    print("\nFinal Amida Diagram:")
    print_amida(amida, players)

    results = simulate_paths(amida, players)
    print("Player Results:")
    for player, result in results.items():
        print(f"Player {player + 1} ends up at column {result + 1}.")

if __name__ == "__main__":
    main()