#!/usr/bin/env python
# Module for unit testing cookie_function module functions
import unittest

# Import functions from our main file for test
from cookie_functions import mostActiveCookies

class TestMostActiveCookie(unittest.TestCase):
  # Unit tests:

  # Test date with only one most occuring
  def test_one(self):
    self.assertEqual(
      mostActiveCookies("test_file.txt", "2022-12-10"), 
      [
      "msvEYZgZy3x8MSCB"
      ], 
      """Should be 
      msvEYZgZy3x8MSCB
      """
    )

  # Test date with 3 most occuring
  def test_two(self):
    self.assertEqual(
      mostActiveCookies("test_file.txt", "2022-01-02"), 
      [
      "pjju6dopXcPE35b6", 
      "xXhuxDcdgBxODvHX", 
      "lyMEDq9YnbBN3gye"
      ], 
      """
      Should be 
      pjju6dopXcPE35b6, 
      xXhuxDcdgBxODvHX, 
      lyMEDq9YnbBN3gye
      """
    )

  # Test date with every packet occuring equally
  def test_three(self):
    self.assertEqual(
      mostActiveCookies("test_file.txt", "2022-06-14"), 
      [
        "NJlPZmU5ts9LfYKI", 
        "qGy8V4Q4hTvfpnx3", 
        "EKBOiCc9uynNBqqh", 
        "Ws8oRKDuxhzKftK5", 
        "edQ6WZghGq5tpdVX", 
        "QQxxy0ru5jAytTRO", 
        "MfqHtuGFmsbBg966", 
        "DRSrznilPxNd38o6", 
        "wiWv0Q698XeIoPfU"
      ], 
      """
      Should be 
      NJlPZmU5ts9LfYKI, 
      qGy8V4Q4hTvfpnx3, 
      EKBOiCc9uynNBqqh, 
      Ws8oRKDuxhzKftK5, 
      edQ6WZghGq5tpdVX, 
      QQxxy0ru5jAytTRO, 
      MfqHtuGFmsbBg966, 
      DRSrznilPxNd38o6, 
      wiWv0Q698XeIoPfU
      """
    )
  
  # Test date with only 2 most occuring
  def test_four(self):
    self.assertEqual(
      mostActiveCookies("test_file.txt", "2022-09-22"), 
      [
        "oYPQ2ryayy8GtNc9", 
        "sCU2V6vuixQoxOmR"
      ], 
      """
      Should be 
      oYPQ2ryayy8GtNc9, 
      sCU2V6vuixQoxOmR
      """
    )

  # Test date with no packets occuring
  def test_five(self):
    self.assertEqual(
      mostActiveCookies("test_file.txt", "2002-09-22"), 
      [
      ], 
      """
      Should be empty
      """
    )

  # Test different date with only one occuring
  def test_six(self):
    self.assertEqual(
      mostActiveCookies("test_file.txt", "2022-12-10"), 
      [
        "msvEYZgZy3x8MSCB"
      ], 
      """
      Should be msvEYZgZy3x8MSCB
      """
    ) 

if __name__ == '__main__':
  # Run our unit tests to make sure functions in the module are working correctly
  unittest.main()
