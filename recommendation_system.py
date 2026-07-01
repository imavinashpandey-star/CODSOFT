# ===============================
# CODSOFT Internship - Task 3
# Recommendation System
# ===============================
MOVIES = {
    "Action": [
        "The Dark Knight",
        "John Wick",
        "Avengers: Endgame",
        "Mad Max: Fury Road",
        "Mission: Impossible – Fallout"
    ],
    "Comedy": [
        "3 Idiots",
        "The Hangover",
        "Welcome",
        "Free Guy",
        "Jumanji: Welcome to the Jungle"
    ],
    "Horror": [
        "The Conjuring",
        "Annabelle",
        "IT",
        "Insidious",
        "Hereditary"
    ],
    "Romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Me Before You",
        "Pride & Prejudice"
    ],
    "Science Fiction": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Arrival",
        "Blade Runner 2049"
    ]
}
def display_header():
    """Display application header."""
    print("=" * 60)
    print("        🎬 MOVIE RECOMMENDATION SYSTEM 🎬")
    print("=" * 60)
    print("Find great movies based on your favorite genre!\n")
def display_genres():
    """Display all available genres."""
    print("Available Genres")
    print("-" * 20)

    for index, genre in enumerate(MOVIES.keys(), start=1):
        print(f"{index}. {genre}")

    print()
def recommend_movies():
    """Recommend movies based on user choice."""

    while True:

        display_genres()

        choice = input("Enter your favorite genre: ").strip().title()

        print()

        if choice in MOVIES:

            print(f"Recommended {choice} Movies")
            print("-" * 35)

            for number, movie in enumerate(MOVIES[choice], start=1):
                print(f"{number}. {movie}")

        else:
            print("Invalid Genre!")
            print("Please choose a genre from the available list.")

        again = input("\nWould you like another recommendation? (yes/no): ").strip().lower()

        while again not in ["yes", "no"]:
            again = input("Please enter 'yes' or 'no': ").strip().lower()

        if again == "no":
            print("\nThank you for using the Movie Recommendation System!")
            print("Enjoy your movies! 🍿")
            break

        print("\n" + "=" * 60 + "\n")
def main():
    display_header()
    recommend_movies()

if __name__ == "__main__":
    main()
