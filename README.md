# Visual CryptograPY

This repository contains a Python implementation of **Visual Cryptography** schemes from binary up to 8-level greyscale images.

The library allows for the encryption of images into two separate "shares." When superimposed, these shares reveal the original image without requiring any complex cryptographic computation—the human visual system performs the decryption "mechanically."

## 📖 Theoretical Background

### 1. Binary Images (Naor & Shamir Scheme)

Based on the 1994 paper by Moni Naor and Adi Shamir, this scheme encrypts a black-and-white secret image into two transparent shares consisting of random noise.

* **Encryption:** Each pixel of the original image is expanded into two identical or complementary $2 \times 2$ grids in the two output shares.
* **Decryption:** The original information can be restored by physically overlaying the 2 shares:
  * If two correspondent grids are identical, the eye perceives them as a grey (half-white, half-black) area.
  * If two correspondent grids are complementary, the area appears completely black.
* **Security:** The system offers **Perfect Secrecy** (similar to the One-Time Pad). An individual share reveals no significant information about the original image.

### 2. Grayscale Images (4 and 8 Levels)

This project extends the classic binary scheme to grayscale images by using larger grids and simulating the grey intensity by modulating the number of opaque pixels on the superimposed result:

* **Preprocessing:** The input image is quantized to 4 or 8 shades of gray. **Floyd-Steinberg dithering** is applied to distribute quantization error and improve visual quality.
* **Pixel Expansion:**
  * **4 Levels:** Pixels are expanded into $3 \times 3$ matrices (9 subpixels).
  * **8 Levels:** Pixels are expanded into $4 \times 4$ matrices (16 subpixels).


* **Mechanism:** The number of transparent pixels remaining after the overlay determines the brightness (gray level) perceived by the user.

You can check `Visual_CryptograPY.pdf` for further details about the visual cryptography schemes.

## 🚀 Installation & Usage

The easiest way to try the library is through the Gradio web interface.

1. Install the dependencies:
```bash
pip install opencv-python
pip install gradio
```
If you encounter dependency problems while installing `opencv-python`, you can try:
```bash
pip install opencv-python-headless
```

2. Clone the repository.
3. Run the application:
```bash
python GUI.py
```


4. Open your browser at `http://127.0.0.1:8080` (you can use a different port by editing the `server_port` attribute at the end of `GUI.py`).

### Using Docker

You can also run the application in a container without installing dependencies manually.

1. **Build the image:**
```bash
docker build -t visual-crypto .
```


2. **Run the container:**
```bash
docker run -p 8080:8080 visual-crypto
```



## 🖥️ Interface Guide

The Gradio interface is divided into 3 main tabs:

### 1. Encrypt

You can upload your input image and choose your preferred modality (`Binary`, `4 Levels Greyscale` or `8 Level Greyscale`).
After running the encryption process, the user is provided with the encrypted image and the randomly generated key, both in the same domain of the quantized image (not yet overlayable).



### 2. VC Conversion

The user can upload a previously generated share and apply the needed conversion to make it overlayable.

### 3. Superimpose

The user can upload two shares to simulate the physical superimposition. The same result can be obtained by digitally overlaying the two images on an image editing tool or even by printing the two shares on transparent sheets.
