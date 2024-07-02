import pathlib
from PIL import Image, ImageDraw, ImageFont

FONT = "Space Mono Bold Italic for Powerline.ttf"

def generate_invites():
    pathlib.Path("invites").mkdir(exist_ok=True)
    font = ImageFont.truetype(FONT, size=70)
    with open("guest-list.txt", 'r') as file:
        print(f"Creating invites for:")
        template = Image.open("invite-template.png")
        for to_whom in file:
            print(f"• {to_whom.strip()}")
            personalized = template.copy()
            d = ImageDraw.Draw(personalized)
            d.text((50,30), to_whom, font=font, fill=(0,50,150), stroke_width=3)
            personalized.save(f"invites/{to_whom.strip()}.png")

# Call the main function
if __name__ == "__main__":
    generate_invites()