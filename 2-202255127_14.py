{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled66.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMAHrpy4TF+b+lZDnSByR3G",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week13/blob/main/2-202255127_14.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lc1wL6fuxxKY",
        "outputId": "f925b5b1-f967-43ca-8ee2-2cdc5e87d0ab"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "1 3 2 6 8\n",
            "1 2 2 3 4 "
          ]
        }
      ],
      "source": [
        "N=int(input())\n",
        "B= list(map(int,input().split()))\n",
        "for T in range(1,N+1):\n",
        "    if T==1:\n",
        "      r= B[0]\n",
        "      print(r,end=' ')\n",
        "    else:\n",
        "      b=B[:T]\n",
        "      R=sum(b)\n",
        "      r=R//T\n",
        "      print(r,end=' ')"
      ]
    }
  ]
}