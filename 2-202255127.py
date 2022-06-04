{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMmo7OnKqlV6z0Sqn/XvrJC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week13/blob/main/2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JTppRe55NG02",
        "outputId": "22257246-aff0-40d1-cf6a-59d091b1674a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "23442\n",
            "75\n",
            "00\n"
          ]
        }
      ],
      "source": [
        "N = input()\n",
        "F = int(input())\n",
        "a = int(N[:-2] + '00')\n",
        "while True:\n",
        "    if a % F == 0:\n",
        "        break\n",
        "    a += 1\n",
        "print(str(a)[-2:])"
      ]
    }
  ]
}