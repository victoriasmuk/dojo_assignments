function pizzeria(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crust = crustType;
    pizza.sauce = sauceType;
    pizza.cheese = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
var pizza1 = pizzeria("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"])
var pizza2 = pizzeria("hand tossed", "marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"])
var pizza3 = pizzeria("thin", "ranch", ["mozzarella"],["chicken","bacon"])
var pizza4 = pizzeria("traditional","red",["fresh mozzarella"],["basil","olive oil"])
console.log(pizza1, pizza2, pizza3, pizza4)
