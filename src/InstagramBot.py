from instabot import Bot
import getpass
import os 
import glob



user = input("Enter your username :  ")
pwd = getpass.getpass(f"Enter password for user {user} => " )

# cookie_del = glob.glob("config/*cookie.json") # This will remove unwanted cookies that prevent login
# os.remove(cookie_del[0])


bot = Bot()
bot.login(username = user, password = pwd)

def UploadPhoto():
    img = "/media/dell-insp/New Volume/CODES/Python/Image/pexels-pixabay-220769.jpg"
    if ask := input("Do you want caption (yes/no): ").lower() == "yes":
        caption = input("Enter the caption: ")
    else : 
        caption = None
    bot.upload_photo(img, caption)
def Follow():
    other = input("Type username of the user you want to follow: ")
    bot.follow(user, other)
    print(f"Followed {other} successfully.")
        
def Unfollow():

        if (ask := input("Do you want unfollow everyone (yes/no)" ).lower() )!= "yes":
            bot.unfollow_all(user)
        elif ask == "no":
            other = input("Type user name of other user to unfollow: ")
            bot.unfollow(user, other)
            print(f"Unfollowed {other} User Successfully")
def CountFollowers():
    print(f"Total number of followers of user {user} are", len(bot.get_user_followers(user)))
def Like():
    post_link = input("Enter link of other user to like ")
    link = bot.get_media_id_from_link(post_link)
    bot.like(link)
    print("Liked Successfully")
def Comment():
    post_link = input("Enter link of other user to like ")
    link = bot.get_media_id_from_link(post_link)

    message = input("Enter the message" )
    bot.comment(link , message)
    print("Commented Successfully")
def Send_message():    
    message = input("Enter the message" )
    user_names = []
    while ask:=input("Enter the user_name (type quit to exit) :" )!= "quit":
        user_names.append(ask)
    bot.send_messages(message ,user_names )             
def get_user_info():
    if ask := input("Do you want to get user information of all your followers " ):
        for i in bot.get_user_followers(user):
            print(bot.get_user_info(i))
    else:
        other = input("Enter other user to get information")
        print(bot.get_user_info(other))

def main_program():
    print()
    print("Press U for Upload Photo...")
    print("Press F for Follow...")
    print("Press UF for Unfollow...")
    print("Press C for Count Followers...")
    print("Press L for Like a post...")
    print("Press CM for Comment in a post..")
    print("Press S for Send Message...")
    print("Press G for Get User Info...")
    print("Press Q to Quit...")
    print()
    
    while True:
        ask = input("Enter the operation you want to perform: ").upper()
        
        try:
            match ask:
                case "Q":
                    print("Exiting program...")
                    break
                case "U":
                    UploadPhoto()
                case "F":
                    Follow()
                case "UF":
                    Unfollow()
                case "C":
                    CountFollowers()
                case "L":
                    Like()
                case "CM":
                    Comment()
                case "S":
                    Send_message()
                case "G":
                    get_user_info()
                case _:
                    print("Invalid operation. Please try again.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

main_program()



