ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# list
ft_list[1] = "world"

# tuple
ft_tuple_list = list(ft_tuple)
ft_tuple_list[1] = "Morocco"
ft_tuple = tuple(ft_tuple_list)

# set
ft_set.discard('tutu!')
ft_set.add("Khouribga")


# dictionary
ft_dict["Hello"] = "1337"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)