
## 🛠️ Installation

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/)
[![Downloads](https://static.pepy.tech/badge/ultralytics)](https://pepy.tech/project/ultralytics)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

To install the ultralytics package in developer mode, ensure you have Git and Python 3 installed on your system. Then, follow these steps:

1. Clone the ultralytics repository to your local machine using Git:

    ```bash
    git clone https://github.com/ultralytics/ultralytics.git
    ```

2. Navigate to the cloned repository's root directory:

    ```bash
    cd ultralytics
    ```

3. Install the package in developer mode using pip (or pip3 for Python 3):

    ```bash
    pip install -e '.[dev]'
    ```

- This command installs the ultralytics package along with all development dependencies, allowing you to modify the package code and have the changes immediately reflected in your Python environment.

## 🚀 Building and Serving Locally

The `mkdocs serve` command builds and serves a local version of your MkDocs documentation, ideal for development and testing:

```bash
mkdocs serve
```

- #### Command Breakdown:

    - `mkdocs` is the main MkDocs command-line interface.
    - `serve` is the subcommand to build and locally serve your documentation.

- 🧐 Note:

    - Grasp changes to the docs in real-time as `mkdocs serve` supports live reloading.
    - To stop the local server, press `CTRL+C`.

## 🌍 Building and Serving Multi-Language

Supporting multi-language documentation? Follow these steps:

1. Stage all new language \*.md files with Git:

    ```bash
    git add docs/**/*.md -f
    ```

2. Build all languages to the `/site` folder, ensuring relevant root-level files are present:

    ```bash
    # Clear existing /site directory
    rm -rf site

    # Loop through each language config file and build
    mkdocs build -f docs/mkdocs.yml
    for file in docs/mkdocs_*.yml; do
      echo "Building MkDocs site with $file"
      mkdocs build -f "$file"
    done
    ```

3. To preview your site, initiate a simple HTTP server:

    ```bash
    cd site
    python -m http.server
    # Open in your preferred browser
    ```

- 🖥️ Access the live site at `http://localhost:8000`.

## 📤 Deploying Your Documentation Site

Choose a hosting provider and deployment method for your MkDocs documentation:

- Configure `mkdocs.yml` with deployment settings.
- Use `mkdocs deploy` to build and deploy your site.

* ### GitHub Pages Deployment Example:

    ```bash
    mkdocs gh-deploy
    ```

## 💡 Contribute

We cherish the community's input as it drives Ultralytics open-source initiatives. Dive into the [Contributing Guide](https://docs.ultralytics.com/help/contributing) and share your thoughts via our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt thank you 🙏 to each contributor!

![Ultralytics open-source contributors](https://github.com/ultralytics/assets/raw/main/im/image-contributors.png)

## 📜 License

Ultralytics Docs presents two licensing options:

- **AGPL-3.0 License**: Perfect for academia and open collaboration. Details are in the [LICENSE](https://github.com/ultralytics/docs/blob/main/LICENSE) file.
- **Enterprise License**: Tailored for commercial usage, offering a seamless blend of Ultralytics technology in your products. Learn more at [Ultralytics Licensing](https://ultralytics.com/license).

## ✉️ Contact

For the dataset (InlandVessel/MS2ShipOBB), please contact [617719299@qq.com](mailto:617719299@qq.com).
