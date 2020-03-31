from parse import readJSON

def main():
    data = readJSON("data/01.19-10.19.json")[0]["f"]
    print(data)

if __name__ == "__main__":
    main()