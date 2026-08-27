# Kontrolled Browser

A lightweight desktop web browser built with **Python and PyQt5**.

Kontrolled Browser uses Qt WebEngine to provide a simple browser experience with essential navigation controls, a URL bar, and a clean desktop interface.

## Features

* Web browsing powered by Qt WebEngine
* Home page set to Google
* Back and Forward navigation
* Page Reload
* Editable URL bar
* Automatic URL updates
* Maximized browser window
* Simple and lightweight codebase

## Tech Stack

* **Python**
* **PyQt5**
* **Qt WebEngine**

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/kontrolled-browser.git
cd kontrolled-browser
```

### 2. Install dependencies

Make sure Python is installed, then run:

```bash
pip install PyQt5 PyQtWebEngine
```

### 3. Run the browser

```bash
python Browser.py
```

The application will launch in a maximized window with Google as the default home page.

## How It Works

The browser interface is built around `QWebEngineView`, which handles the actual web content.

The application adds a toolbar containing:

* **Home** to return to Google
* **Reload** to refresh the current page
* **Back** to return to the previous page
* **Forward** to move to the next page
* **URL Bar** to enter and navigate to websites

The URL bar is also automatically updated whenever the current page changes.

## Project Structure

```text
Kontrolled-Browser/
│
├── Browser.py
└── README.md
```

## Current Status

**Early development**

The current version focuses on the core browser experience and provides the basic functionality needed for desktop web browsing.

Future versions may introduce additional browser features such as tabs, bookmarks, history, downloads, themes, and improved navigation.

## Roadmap

* [ ] Tab support
* [ ] Bookmarks
* [ ] Browsing history
* [ ] Download manager
* [ ] Custom homepage
* [ ] Dark mode
* [ ] Keyboard shortcuts
* [ ] Improved URL handling
* [ ] Browser settings
* [ ] Better UI and navigation

## Contributing

Contributions, ideas, and improvements are welcome.

If you find a bug or have an idea for a feature, feel free to open an issue or submit a pull request.

## License

This project is open source. Add a license to the repository if you intend to define specific terms for using, modifying, or distributing the project.

---

**Kontrolled Browser**
Built with Python and PyQt5.
