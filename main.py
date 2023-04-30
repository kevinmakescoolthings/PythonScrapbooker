from PIL import Image, ImageDraw, ImageFont
import textwrap

# Location of files
file_dir ='C:\\Users\\kevin\\Documents\\Projects\\Active\\PythonScrapbooking\\'

# Pixel density
pixels_per_inch = 300

# Adding indent to description paragraphs
indent = "    "

# Load fonts
title_font = ImageFont.truetype("arial.ttf", 144)
image_title_font = ImageFont.truetype("arial.ttf", 64)
image_description_font = ImageFont.truetype("arial.ttf", 56)

# Inputs for each scrapbook
front_cover = "FrontCover.png"
back_cover = "BackCover.png"
pages = [
    ["Page 1 Title",
     "CloudBackground.png",
     "template_1",
     "liudmyla-denysiuk-iJ9o00UeAWk-unsplash.jpg",
     "Hedgehogs are Awesome",
     "A hedgehog is a spiny mammal of the subfamily Erinaceinae, in the eulipotyphlan family Erinaceidae. There are seventeen species of hedgehog in five genera found throughout parts of Europe, Asia, and Africa, and in New Zealand by introduction. ",
     "hans-jurgen-mager-qQWV91TTBrE-unsplash.jpg",
     "Polar Bears are Scary",
     "The polar bear (Ursus maritimus) is a hypercarnivorous species of bear. Its native range lies largely within the Arctic Circle, encompassing the Arctic Ocean and its surrounding seas and landmasses, which includes the northernmost regions of North America and Eurasia. It is the largest extant bear species."
     ],
    ["Page 2 Title",
     "CloudBackground.png",
     "template_2",
     "liudmyla-denysiuk-iJ9o00UeAWk-unsplash.jpg",
     "Hedgehogs are Adorable",
     "A hedgehog is a spiny mammal of the subfamily Erinaceinae, in the eulipotyphlan family Erinaceidae. There are seventeen species of hedgehog in five genera found throughout parts of Europe, Asia, and Africa, and in New Zealand by introduction. ",
     "kote-puerto-so5nsYDOdxw-unsplash.jpg",
     "Kittens are Cute",
     "A kitten is a juvenile cat. After being born, kittens display primary altriciality and are fully dependent on their mothers for survival. They normally do not open their eyes for seven to ten days."
     ]
]

# Resizes and crops images if necessary
def resizeImage(img: Image, resize_w: int, resize_h: int):
 # Get the image dimensions
 img_w, img_h = img.size

 # Check if the aspect ratio is perfect
 if resize_w/resize_h == img_w/img_h:
  # Aspect ratio is correct
  return img.resize((resize_w, resize_h))
 else:
  # Aspect ratio is wrong

  # Resize the image so one dimension is correct (width or height) and the other is oversized
  multiplier_for_w = resize_w / img_w
  multiplier_for_h = resize_h / img_h

  # Determine if it's width or height which should be oversized
  if img_h * multiplier_for_w < resize_h:
   oversized_w = int(img_w * multiplier_for_h)
   resized = img.resize((oversized_w, resize_h))
   excess = int(((img_w * multiplier_for_h) - resize_w) / 2)
   return resized.crop((excess, 0, excess + resize_w, resize_h))
  else:
   oversized_h = int(img_h * multiplier_for_w)
   resized = img.resize((resize_w, oversized_h))
   excess = int((oversized_h - resize_h) / 2)
   return resized.crop((0, excess, resize_w, excess + resize_h))

def generatePage(input: [str]):
 title_text = input[0]
 background_file_name = input[1]
 template_name = input[2]

 # Setup background image
 background_img = Image.open(file_dir + background_file_name)
 draw = ImageDraw.Draw(background_img)

 # Add the title
 text_width, text_height = draw.textsize(title_text, title_font)
 width, height = background_img.size
 x = width / 2 - text_width / 2
 draw.text((x, int(0.25 * pixels_per_inch)), title_text, font=title_font, fill='black')

 if template_name == "template_1":
  first_image_file_name = input[3]
  first_image_title = input[4]
  first_image_description = indent + input[5] # Add indent
  second_image_file_name = input[6]
  second_image_title = input[7]
  second_image_description = indent + input[8] # Add indent

  # Define where the various elements go for the first image
  first_image_x = int(0.5 * pixels_per_inch)
  first_image_y = int(1 * pixels_per_inch)
  first_image_width = int(6 * pixels_per_inch)
  first_image_height = int(4 * pixels_per_inch)
  first_image_title_text_width, first_image_title_text_height = draw.textsize(first_image_title, image_title_font)
  first_image_title_x = first_image_x + first_image_width / 2 - first_image_title_text_width / 2
  first_image_title_y = first_image_y + first_image_height
  first_image_description_x = first_image_x
  first_image_description_y = first_image_title_y + first_image_title_text_height

  # Wrap the first image description
  first_wrapper = textwrap.TextWrapper(width=68)
  wrapped_first_image_description = first_wrapper.fill(text=first_image_description)

  # Define where the various elements go for the second image
  second_image_x = int(5.5 * pixels_per_inch)
  second_image_y = int(6.5 * pixels_per_inch)
  second_image_width = int(6 * pixels_per_inch)
  second_image_height = int(4 * pixels_per_inch)
  second_image_title_text_width, second_image_title_text_height = draw.textsize(second_image_title, image_title_font)
  second_image_title_x = second_image_x + second_image_width / 2 - second_image_title_text_width / 2
  second_image_title_y = second_image_y + second_image_height
  second_image_description_x = second_image_x
  second_image_description_y = second_image_title_y + second_image_title_text_height

  # Wrap the first image description
  second_wrapper = textwrap.TextWrapper(width=68)
  wrapped_second_image_description = second_wrapper.fill(text=second_image_description)

  # Add first image
  first_image = Image.open(file_dir+first_image_file_name)
  first_image_resized = resizeImage(first_image, first_image_width, first_image_height) #first_image.resize((first_image_width, first_image_height))
  background_img.paste(first_image_resized, (first_image_x, first_image_y))

  # Add first image title
  draw.text((first_image_title_x, first_image_title_y), first_image_title, font=image_title_font, fill='black')

  # Add first image description
  draw.text((first_image_description_x, first_image_description_y), wrapped_first_image_description, font=image_description_font, fill='black')

  # Add second image
  second_image = Image.open(file_dir+second_image_file_name)
  second_image_resized = resizeImage(second_image, second_image_width, second_image_height) #second_image.resize((second_image_width, second_image_height))
  background_img.paste(second_image_resized, (second_image_x, second_image_y))

  # Add second image title
  draw.text((second_image_title_x, second_image_title_y), second_image_title, font=image_title_font, fill='black')

  # Add second image description
  draw.text((second_image_description_x, second_image_description_y), wrapped_second_image_description, font=image_description_font, fill='black')

 if template_name == "template_2":
  first_image_file_name = input[3]
  first_image_title = input[4]
  first_image_description = indent + input[5]  # Add indent
  second_image_file_name = input[6]
  second_image_title = input[7]
  second_image_description = indent + input[8]  # Add indent

  # Define where the various elements go for the first image
  first_image_x = int(5.5 * pixels_per_inch)
  first_image_y = int(1 * pixels_per_inch)
  first_image_width = int(6 * pixels_per_inch)
  first_image_height = int(4 * pixels_per_inch)
  first_image_title_text_width, first_image_title_text_height = draw.textsize(first_image_title, image_title_font)
  first_image_title_x = first_image_x + first_image_width / 2 - first_image_title_text_width / 2
  first_image_title_y = first_image_y + first_image_height
  first_image_description_x = first_image_x
  first_image_description_y = first_image_title_y + first_image_title_text_height

  # Wrap the first image description
  first_wrapper = textwrap.TextWrapper(width=68)
  wrapped_first_image_description = first_wrapper.fill(text=first_image_description)

  # Define where the various elements go for the second image
  second_image_x = int(0.5 * pixels_per_inch)
  second_image_y = int(6.5 * pixels_per_inch)
  second_image_width = int(6 * pixels_per_inch)
  second_image_height = int(4 * pixels_per_inch)
  second_image_title_text_width, second_image_title_text_height = draw.textsize(second_image_title, image_title_font)
  second_image_title_x = second_image_x + second_image_width / 2 - second_image_title_text_width / 2
  second_image_title_y = second_image_y + second_image_height
  second_image_description_x = second_image_x
  second_image_description_y = second_image_title_y + second_image_title_text_height

  # Wrap the first image description
  second_wrapper = textwrap.TextWrapper(width=68)
  wrapped_second_image_description = second_wrapper.fill(text=second_image_description)

  # Add first image
  first_image = Image.open(file_dir + first_image_file_name)
  first_image_resized = resizeImage(first_image, first_image_width, first_image_height)  # first_image.resize((first_image_width, first_image_height))
  background_img.paste(first_image_resized, (first_image_x, first_image_y))

  # Add first image title
  draw.text((first_image_title_x, first_image_title_y), first_image_title, font=image_title_font, fill='black')

  # Add first image description
  draw.text((first_image_description_x, first_image_description_y), wrapped_first_image_description, font=image_description_font, fill='black')

  # Add second image
  second_image = Image.open(file_dir + second_image_file_name)
  second_image_resized = resizeImage(second_image, second_image_width,
                                     second_image_height)  # second_image.resize((second_image_width, second_image_height))
  background_img.paste(second_image_resized, (second_image_x, second_image_y))

  # Add second image title
  draw.text((second_image_title_x, second_image_title_y), second_image_title, font=image_title_font, fill='black')

  # Add second image description
  draw.text((second_image_description_x, second_image_description_y), wrapped_second_image_description, font=image_description_font, fill='black')

 return background_img.convert("RGB")

def createScrapbook():
 image_list = []

 # Setup front cover
 front_cover_img = Image.open(file_dir + front_cover)

 # Add the pages
 for page in pages:
  image_list.append(generatePage(page))

 back_cover_img = Image.open(file_dir + back_cover)
 image_list.append(back_cover_img.convert("RGB"))

 # Save everything
 front_cover_img.save(r"C:\\Users\\kevin\\Documents\\Projects\\Active\\PythonScrapbooking\\testScrapbook.pdf", save_all=True, append_images=image_list)

createScrapbook()
