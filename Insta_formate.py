def format_follower_count(number):
    if number >= 1000000:
        return f"{number / 1000000:.1f}M"
    elif number >= 1000:
        return f"{number / 1000:.1f}K"
    else:
        return str(number)

followers = int(input("Enter your follower count:- "))
result = format_follower_count(followers)
print("Instagram followers:-", result)
