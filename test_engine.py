import effects



ast = effects.interpreter.parser.parse("gain up to 2 attack cards with a cost of 7 coins from the trash.")
#ast = effects.interpreter.parser.parse("gain up to 2 attack cards with a cost of 7 from the trash.")



#effects.interpreter.EchoEffect().transform(ast)


print(ast.pretty())