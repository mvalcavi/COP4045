import db
from objects import Product, LineItem, Cart


def show_cart(cart):
    if cart.getItemCount() == 0:
        print("There are no items in your cart.\n")
    else:
        line_format1 = "{:<5s} {:<25s} {:>12s} {:>10s} {:>10s}"
        line_format2 = "{:<5d} {:<25s} {:>12.2f} {:>10d} {:>10.2f}"
        print(line_format1.format("Item", "Name", "Your Price", "Total"))
        i = 0
        for item in cart:
            print(line_format2.format(i + 1,
                                      item.product.title,
                                      item.getTotal()))
            i += 1
        print("{:>66.2f}".format(cart.getTotal()))
        print()


def add_item(cart, products):
    number = int(input("Item number: "))
    quantity = int(input("Quantity: "))
    if number < 1 or number > len(products):
        print("No product has that number.\n")
    else:
        product = products[number - 1]
        item = LineItem(product, quantity)
        cart.addItem(item)
        print("Item " + str(cart.getItemCount()) + " was added.\n")


def remove_item(cart):
    number = int(input("Item number: "))
    if number < 1 or number > cart.getItemCount():
        print("The cart does not contain an item " +
              "with that number.\n")
    else:
        cart.removeItem(number - 1)
        print("Item " + str(number) + " was deleted.\n")


def main():
    products = db.get_products()

    cart = Cart()
    while True:
        command = input("Command: ")
        if command == "cart":
            show_cart(cart)
        elif command == "add":
            add_item(cart, products)
        elif command == "del":
            remove_item(cart)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()

