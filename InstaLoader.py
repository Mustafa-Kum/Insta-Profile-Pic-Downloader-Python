import instaloader

loader = instaloader.Instaloader()

user = input("Enter username : ")

loader.download_profile(user, profile_pic_only = True)