import csv
import requests from bs4 import BeautifulSoup

def get_pinterest_images(tags):
    base_url = f"https://www.pinterest.com/search/pins/?q={'+'.join(tags)}"
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        image_urls = []

        #find image urls in the html using appropriate selectors
        image_elements = soup.find_all('img', {'src': True})

        for img in image_elements:
            image_urls.append(img['src'])

        return image_urls
    else:
        print("Error", response.status_code)
        return []

def save_to_csv(image_urls, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image URLs'])

        for url in image_urls:
            csv_writer.writerow([url])

if __name__ == "__main__":
    tags = input("Enter Pinterest tages (comma-separated): ").split(',')
    image_urls = get_pinterest_images(tags)

    if image_urls:
        output_filename = "pinterest_images.csv"
        save_to_csv(image_urls, output_filename)
        print(f"Image URLs saved to {output_filename}")
    else:
        print("No image URLs found.")
