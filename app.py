from doctr.io import DocumentFile
from doctr.models import ocr_predictor

doc = DocumentFile.from_images("img5.PNG")
print(f"Number of pages: {len(doc)}")

#import matplotlib.pyplot as plt
#plt_1 = plt.figure(figsize=(5, 5))
#plt.imshow(doc[0])
#plt.show()

ocr = ocr_predictor(pretrained=True)

result = ocr(doc)
#print(result)
json_response = result.export()

for words in json_response["pages"][0]["blocks"][0]["lines"][0]["words"]:
    #print(words)
    print(words["value"])

# Function to recursively extract word values
def extract_word_values(data):
    word_values = []
    if isinstance(data, list):
        for item in data:
            word_values.extend(extract_word_values(item))
    elif isinstance(data, dict):
        if "words" in data:
            word_values.extend(word["value"] for word in data["words"])
        else:
            for key, value in data.items():
                word_values.extend(extract_word_values(value))
    return word_values

# Extract word values
word_values = extract_word_values(json_response)

# Print all word values
for word_value in word_values:
    print(word_value)