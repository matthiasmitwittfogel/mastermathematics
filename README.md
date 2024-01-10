# mastermathematics Manim Code Repository

Welcome to the GitHub repository for [mastermathematics](https://www.youtube.com/channel/UCJ0KfcrJnTDGwFDXcPe6MZQ), where I use the power of ManimCE to create stunning mathematical videos. If you enjoy visual math and engaging explanations, be sure to check out and **subscribe to my YouTube channel** for the latest content!

[![Subscribe to mastermathematics](https://img.shields.io/youtube/channel/subscribers/UCJ0KfcrJnTDGwFDXcPe6MZQ?style=social&label=Subscribe%20to%20mastermathematics)](https://www.youtube.com/channel/UCJ0KfcrJnTDGwFDXcPe6MZQ)
![Videos](https://img.shields.io/youtube/channel/views/UCJ0KfcrJnTDGwFDXcPe6MZQ?style=social)

![Manim Version](https://img.shields.io/badge/Manim%20CE-0.17-blueviolet)
![Manim Version](https://img.shields.io/pypi/v/manimce?label=manim)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Code Size](https://img.shields.io/github/languages/code-size/matthiasmitwittfogel/mastermathematics)
![Downloads](https://img.shields.io/github/downloads/matthiasmitwittfogel/mastermathematics/total)
![GitHub Issues](https://img.shields.io/github/issues/matthiasmitwittfogel/mastermathematics)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/matthiasmitwittfogel/mastermathematics)
[![Last Commit](https://img.shields.io/github/last-commit/matthiasmitwittfogel/mastermathematics)](https://github.com/matthiasmitwittfogel/mastermathematics)
[![License](https://img.shields.io/github/license/matthiasmitwittfogel/mastermathematics)](https://github.com/matthiasmitwittfogel/mastermathematics/blob/main/LICENSE)


Welcome to the GitHub repository where I store all of the Manim code used to create educational math videos for my YouTube channel [mastermathematics](https://www.youtube.com/channel/UCJ0KfcrJnTDGwFDXcPe6MZQ). Here, you can find the code corresponding to each video, allowing you to explore and learn the magic behind the animations.

## Build Instructions

To generate the videos included in this repository, follow these steps:

1. Install ManimCE according to the [installation guide](https://docs.manim.community/en/stable/installation.html) on the official Manim documentation page.
2. Some videos include voiceovers. To add voiceovers, install the requirements using the [Manim voiceover guide](https://docs.manim.community/en/stable/guides/add_voiceovers.html).
3. For Azure voiceover API integration, populate the `.env` file with your Azure API keys following the instructions on the [Manim Voiceover AzureService page](https://voiceover.manim.community/en/latest/services.html).
4. To generate videos, execute the command `manim -pql [filename]`. Adjust command-line options for Manim as needed for different resolutions or behaviors.

## Repository Contents

Below is a directory of Python scripts and their corresponding YouTube videos:
    
| File Name                                                                                       | YouTube Link                                                      | Content Description                                          |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------|
| [20230905_apple_logo.py](shorts%2F20230905_apple_logo.py)                                       | [Watch](https://www.youtube.com/shorts/_JcG53_koAc)               | Animating the Apple logo with geometry                       |
| [20230907_sum_from_1_to_n.py](shorts%2F20230907_sum_from_1_to_n.py)                             | [Watch](https://www.youtube.com/shorts/DcpvZphAmtE)               | Visualizing the sum from 1 to n                              |
| [20230907_sum_from_1_over_2_to_1_over_64.py](shorts%2F20230907_sum_from_1_over_2_to_1_over_64.py)| [Watch](https://www.youtube.com/shorts/pZ9D7cVGfXg)               | Sum of series from 1/2 to 1/64                               |
| [20230909_a_plus_b_square.py](shorts%2F20230909_a_plus_b_square.py)                             | [Watch](https://www.youtube.com/shorts/6YCmP_YI2y0)               | Illustrating the (a+b)² formula                              |
| [20230910_difference_of_squares.py](shorts%2F20230910_difference_of_squares.py)                 | [Watch](https://www.youtube.com/shorts/7xLBwvQVkks)               | Difference of squares visualization                          |
| [20230913_find_shaded_area.py](shorts%2F20230913_find_shaded_area.py)                           | [Watch](https://www.youtube.com/shorts/hM80vKYMGyY)               | Finding the area of a shaded region                          |
| [20230916_bubble_sort_algorithm.py](shorts%2F20230916_bubble_sort_algorithm.py)                 | [Watch](https://www.youtube.com/shorts/DdLTrfpylfw)               | Demonstrating the bubble sort algorithm                      |
| [20230919_circle_area.py](shorts%2F20230919_circle_area.py)                                     | [Watch](https://www.youtube.com/shorts/llM5NW0j-k0)               | Explaining the calculation of a circle's area                |
| [20230925_sum_from_1_to_2n_1.py](shorts%2F20230925_sum_from_1_to_2n_1.py)                       | [Watch](https://www.youtube.com/shorts/-1SY4wm9QNQ)               | Summing an arithmetic sequence up to (2n-1)                  |
| [20230927_sum_1_to_n_to_1.py](shorts%2F20230927_sum_1_to_n_to_1.py)                             | [Watch](https://www.youtube.com/shorts/XTVIPywgwDY)               | Summing reciprocals from 1 to n                              |
| [20231001_febonacci_square_sum.py](shorts%2F20231001_febonacci_square_sum.py)                   | [Watch](https://www.youtube.com/shorts/g17zLAkW4iA)               | Visualization of Fibonacci sequence and its square sum       |
| [20231003_series_sum_from_one_over8.py](shorts%2F20231003_series_sum_from_one_over8.py)         | [Watch](https://www.youtube.com/shorts/pRvgyhpcdII)               | Series summation starting at 1/8                             |
| [20231008_a_plus_b__plus_c_square.py](shorts%2F20231008_a_plus_b__plus_c_square.py)             | [Watch](https://www.youtube.com/shorts/PXQgORj1AQo)               | Visualization of the (a+b+c)² formula                        |
| [20231008_insertion_sort_animation.py](shorts%2F20231008_insertion_sort_animation.py)           | [Watch](https://www.youtube.com/shorts/4cmuJJISfPY)               | Animation of the insertion sort sorting method               |
| [20231010_selection_sort.py](shorts%2F20231010_selection_sort.py)                               | [Watch](https://www.youtube.com/shorts/yPilRFA2ZMM)               | Demonstrating the selection sort algorithm                   |
| [20231021_infinite_series_from_1_over_2.py](shorts%2F20231021_infinite_series_from_1_over_2.py) | [Watch](https://www.youtube.com/shorts/eFJHXx-xyZ0)               | Infinite series starting at 1/2 visualized                   |
| [20231025_1_over_3_series.py](shorts%2F20231025_1_over_3_series.py)                             | [Watch](https://www.youtube.com/shorts/OhZ4BSQNqUU)               | Series summation starting at 1/3                             |
| [20231025_express_love_with_formulas](videos%2F20231025_express_love_with_formulas)             | [Watch](https://www.youtube.com/watch?v=v_xEl70TM8c)              | Expressing affection through mathematical formulas           |
| [20231031_bytedance_logo.py](shorts%2F20231031_bytedance_logo.py)                               | [Watch](https://www.youtube.com/shorts/JuBcZKQRv_w)               | Geometry-based animation of the ByteDance logo               |
| [20231104_cube_sum](videos%2F20231104_cube_sum)                                                 | [Watch](https://www.youtube.com/watch?v=r5itGj29gh8&t=24s)        | Summation of cubes formula shown visually                    |
| [20231107_china_flag](videos%2F20231107_china_flag)                                             | [Watch](https://www.youtube.com/watch?v=G3FpbKVKlCg)              | Creating the flag of China through animations                |


## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Contact Information

If you have any questions, suggestions, or encounter any issues with the compilation, please feel free to reach out to me:

- 📧 **Email**: [matthiaswittfogel@gmail.com](mailto:matthiaswittfogel@gmail.com)

Your feedback is highly appreciated and will help me improve this project!


## Acknowledgments

Special thanks to the [Manim Community](https://www.manim.community/) for creating a powerful tool that makes math visualizations accessible and engaging.

---
