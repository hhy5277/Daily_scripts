#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
import logging
import re

import requests


def log():
    logging.basicConfig(filename='drcom.log',
                        level=logging.DEBUG,
                        format='[%(levelname)s] [%(asctime)s',
                        datefmt='%d/%b/%y %H:%M:%S')
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)-6s[%(asctime)s]]: %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger('').addHandler(handler)
    return logging

def read_config(config_path):
    configs = ConfigParser.ConfigParser()
    configs.read(config_path)
    count = configs.get('userinfo', 'count')
    password = configs.get('userinfo', 'enpassword')
    config_dict = {'count': count,
                   'password': password}
    return config_dict


class Drcom:

    LOG = log()
    configs = read_config('config.ini')
    count = configs.get('count')
    password = configs.get('password')
    host = "http://202.112.208.3/"
