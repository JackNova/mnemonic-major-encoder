#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `mnemonic_major_encoder` package."""

import pytest
import string
import sys
import re

from mnemonic_major_encoder import encoder


def codes_helper(code, should_pass, should_not_pass):
    for s in should_pass:
        assert encoder.CODES[code].fullmatch(s)

    for s in should_not_pass:
        assert encoder.CODES[code].fullmatch(s) is None


def test_capture_0():
    should_pass = ['sce', 'sci', 'ss', 'zz', 's', 'z']
    should_not_pass = ['scei', 'scie', 'sss', 'zzz', 'sz', 'zs']
    codes_helper(0, should_pass, should_not_pass)


def test_capture_1():
    should_pass = ['tt', 'dd', 't', 'd']
    should_not_pass = ['ttt', 'dt', 'ddd', 'td']
    codes_helper(1, should_pass, should_not_pass)


def test_capture_2():
    should_pass = ['nn', 'gn', 'n']
    should_not_pass = ['nnn', 'gnn', 'ng']
    codes_helper(2, should_pass, should_not_pass)


def test_capture_3():
    should_pass = ['mm', 'm']
    should_not_pass = ['mmm']
    codes_helper(3, should_pass, should_not_pass)


def test_capture_4():
    should_pass = ['rr', 'r']
    should_not_pass = ['rrr']
    codes_helper(4, should_pass, should_not_pass)


def test_capture_5():
    should_pass = ['ll', 'gl', 'l']
    should_not_pass = ['lll', 'lg', 'ggl']
    codes_helper(5, should_pass, should_not_pass)


def test_capture_6():
    should_pass = ['ce', 'ci', 'cce', 'cci', 'ge', 'gi', 'gge', 'ggi', 'j']
    should_not_pass = [
        'cee', 'cii', 'ccce', 'ccci', 'gce', 'gci', 'ggge', 'gggi', 'gj'
    ]
    codes_helper(6, should_pass, should_not_pass)


def test_capture_7():
    should_pass = [
        'cc', 'gg', 'qq', 'kk', 'ck', 'ch', 'cq', 'c', 'g', 'q', 'k'
    ]
    should_not_pass = [
        'ccc', 'ggg', 'qqq', 'kkk', 'ckk', 'chh', 'cqq', 'kc', 'qg', 'gq', 'gk'
    ]
    codes_helper(7, should_pass, should_not_pass)


def test_capture_8():
    should_pass = ['ff', 'vv', 'f', 'v']
    should_not_pass = ['fff', 'vvv', 'fv', 'vf']
    codes_helper(8, should_pass, should_not_pass)


def test_capture_9():
    should_pass = ['pp', 'bb', 'p', 'b']
    should_not_pass = ['ppp', 'bbb', 'bp', 'pb']
    codes_helper(9, should_pass, should_not_pass)
