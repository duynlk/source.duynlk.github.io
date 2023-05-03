import os
import locale

locale.setlocale(locale.LC_COLLATE, 'vi_VN')
postsPath = 'content/posts'
muclucPath = 'content/muc-luc.md'
posts = []

for fileName in os.listdir(postsPath):
	realPath = os.path.join(postsPath, fileName)
	if os.path.isfile(realPath):

		# bypass muc-luc.md
		if fileName == "muc-luc.md":
			continue

		# get title and contest
		fileOpen = open(realPath, 'r', encoding="utf8")
		lines = fileOpen.readlines()
		lineNumber = 0
		isContest = False
		isTranslatePoem = False
		isTranslateMusic = False

		for ln in lines:
			if lineNumber > 5:
				break

			lineContent = ln.strip()

			# get title
			if lineNumber == 1:
				title = lineContent.replace("title: ", "").replace("\"", "")

			# get contest
			if lineNumber == 3 and "contest: true" in lineContent:
				isContest = True

			# get translate poem
			if lineNumber == 4 and "translate-poem: true" in lineContent:
				isTranslatePoem = True

			# get translate music
			if lineNumber == 5 and "translate-music: true" in lineContent:
				isTranslateMusic = True

			lineNumber += 1

		# get url
		url = fileName.replace(".md", "")

		# make small-list
		post = []
		post.append(title)
		post.append(url)
		post.append(isContest)
		post.append(isTranslatePoem)
		post.append(isTranslateMusic)

		# assign big-list
		posts.append(post)

# sort name a-z
sorted(posts)

# clear file
with open(muclucPath,'w') as file:
	pass

# write file
fileWrite = open(muclucPath, "w", encoding="utf8")
fileWrite.write("---\n")
fileWrite.write("title: \"Mục Lục\"\n")
fileWrite.write("---\n")

rank = 1
for ps in posts:
	contestText = ""
	if ps[2] == True:
		contestText = " *(Bài dự thi)*"
	if ps[3] == True:
		contestText = " *(Dịch thơ)*"
	if ps[4] == True:
		contestText = " *(Dịch nhạc)*"
	content = str(rank) + ". [" + ps[0] + "](/posts/" + ps[1] + ")" + contestText + "\n"
	fileWrite.write(content)
	rank += 1

fileWrite.close()