# Produce by Joshua

# University of Aberdeen

# Development time: 2023/3/4 2:27

src_file = open('backgroud.png','rb')
target_file = open('new_image_bg.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()
