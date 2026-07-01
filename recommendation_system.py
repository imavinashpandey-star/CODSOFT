# Simple Recommendation System

movies = {
    "Action": [
        "Avengers: Endgame",
        "John Wick",
        "The Dark Knight"
    ],
    "Comedy": [
        "3 Idiots",
        "The Hangover",
        "Welcome"
    ],
    "Horror": [
        "The Conjuring",
        "Annabelle",
        "IT"
    ],
    "Romance": [
        "Titanic",
        "The Notebook",
        "La La Land"
    ],
    "Science Fiction": [
        "Interstellar",
        "Inception",
        "The Matrix"
    ]
}

print("=" * 40)
print("Movie Recommendation System")
print("=" * 40)

print("\nAvailable Categories:")
for category in movies:
    print("-", category)

choice = input("\nEnter your favorite category: ").title()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("•", movie)
else:
    print("\nSorry! Category not found.")
    print("Please choose from the available categories.")
