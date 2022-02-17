def validInt(string):
    try:
        int(string)
        return True
    except:
        return False


def validFloat(string):
    try:
        float(string)
        return True
    except:
        return False


def outputRanks(pages: dict, d: float, start: int, iterations: int):
    for page in pages:
        pages[page]["pr"] = start

    for i in range(iterations):
        print("=======================================")
        print("Iteration: {}\n".format(i + 1))
        for A in pages:
            prA = (1 - d)
            for Ti in pages:
                if (Ti != A) and (A in pages[Ti]["outgoing"]):
                    prTi = pages[Ti]["pr"]
                    cTi = len(pages[Ti]["outgoing"])
                    prA += (d * (prTi / cTi))
            print("pr(" + A + ") = " + str(prA))
            pages[A]["pr"] = prA

    total = 0
    for page in pages:
        total += pages[page]["pr"]
    print("\ntotal pr: " + str(total))
    print("average pr: " + str(total / len(pages)))

    print("=======================================")


TERMINATE = "@"


def main():
    pages = {}
    page = input("Enter a page: ")
    while page != TERMINATE:
        outgoing = []
        print('Outgoing connections for "{}":\n{}'.format(page, outgoing))
        otherPage = input('\nEnter a page that "{}" is pointing to: '.format(page))
        while otherPage != TERMINATE:
            outgoing.append(otherPage)
            print('Outgoing connections for "{}":\n{}'.format(page, outgoing))
            otherPage = input('\nEnter a page that "{}" is pointing to: '.format(page))
        print('Outgoing connections for "{}":\n{}'.format(page, outgoing))

        pages[page] = {}
        pages[page]["outgoing"] = outgoing
        page = input("\nEnter a page: ")

    if pages != {}:
        damping = input("\nEnter a damping factor (d): ")
        while not validFloat(damping):
            print("Invalid float!")
            damping = input("Enter a damping factor (d): ")

        start = input("\nEnter a starting guess for page ranks: ")
        while not validInt(start):
            print("Invalid integer!")
            start = input("Enter a starting guess for page ranks: ")

        iterations = input("\nEnter the number of iterations: ")
        while not validInt(iterations):
            print("Invalid integer!")
            iterations = input("Enter the number of iterations: ")

        print()
        outputRanks(pages, float(damping), int(start), int(iterations))


if __name__ == '__main__':
    main()
    input()