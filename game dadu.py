import random

def main():
    print("Selamat datang ke permainan teka nombor dadu!")
    print("Dadu akan menghasilkan nombor antara 1 hingga 6.")

    dadu = random.randint(1, 6)
    print (dadu)

    teka = int(input("Teka nombor (1-6): "))


    if teka == dadu:
        print(f"Anda betul! Nombor dadu adalah {dadu}.")
    else:
        print(f"Maaf, nombor dadu adalah {dadu}. Cuba lagi!")

if __name__ == "__main__":
    main()
