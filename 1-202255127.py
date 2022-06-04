{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNxmqVhTMA28XQvFA7ogGhI",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week13/blob/main/1-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ru4kXYiVMU-Z",
        "outputId": "9c2735a7-c50e-43fb-dc3c-fa60625b6da3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "24\n",
            "6\n",
            "39\n",
            "3\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "def liting(A):\n",
        "  n = sum(list(map(int, A)))\n",
        "  if n < 10:\n",
        "    return n\n",
        "  else:\n",
        "    return liting(str(n))\n",
        "\n",
        "while 1:\n",
        "  N=input()\n",
        "  if N == '0':\n",
        "    break\n",
        "  else:\n",
        "    print(liting(N))"
      ]
    }
  ]
}