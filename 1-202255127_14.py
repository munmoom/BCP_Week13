{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled65.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP0lLH9Jm9m3NPTieVpgmVO",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week13/blob/main/1-202255127_14.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def rand():\n",
        "  res=0\n",
        "  for a in range(0,2):\n",
        "    R= random.randrange(1,6)\n",
        "    res+=R\n",
        "    a+=1\n",
        "  return(res)\n",
        "    \n",
        "T=int(input())\n",
        "for i in range(1,T+1):\n",
        "    R=rand()\n",
        "    print(f'Case {i}: {R}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vl_047MJl5PA",
        "outputId": "32febbc9-62c2-44f8-acc9-2cbcc9a22b90"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "Case 1: 4\n",
            "Case 2: 6\n",
            "Case 3: 8\n",
            "Case 4: 7\n",
            "Case 5: 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "T=int(input())\n",
        "for i in range(1,T+1):\n",
        "    tu = map(int, input().split())\n",
        "    R=sum(tu)\n",
        "    print(f'Case {i}: {R}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N8G7JpzGmNKE",
        "outputId": "489a9363-f3b0-41fd-cc44-e8f8534aaba7"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "2 3\n",
            "Case 1: 5\n",
            "5 6\n",
            "Case 2: 11\n",
            "3 1\n",
            "Case 3: 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "T=int(input())\n",
        "for i in range(1,T+1):\n",
        "    a,b = map(int, input().split())\n",
        "    R=a+b\n",
        "    print(f'Case {i}: {R}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YupDggSyovmt",
        "outputId": "00fe36ab-3bc9-4c01-bc7d-cbf0afff0ea7"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "2 5\n",
            "Case 1: 7\n",
            "3 2\n",
            "Case 2: 5\n",
            "1 5\n",
            "Case 3: 6\n"
          ]
        }
      ]
    }
  ]
}