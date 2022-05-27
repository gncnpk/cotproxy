#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""COTProxy Functions."""

import xml.etree.ElementTree as ET

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2022 Greg Albrecht"
__license__ = "Apache License, Version 2.0"


def parse_cot(msg: str) -> ET.Element:
    root = ET.fromstring(msg)
    return root


def parse_cot_multi(msg: str) -> ET.Element:
    root = ET.fromstring("<root>" + msg + "</root>")
    return root


def get_callsign(msg) -> str:
    return msg.find("detail").attrib.get(
        "callsign", msg.find("detail").find("contact").attrib.get("callsign")
    )


def transform_cot(original, transform) -> ET.Element:
    uid = transform.get("uid")
    detail = original.find("detail")
    # assert uid == detail.attrib['uid']

    callsign = transform.get("callsign")
    if callsign:
        original.find("detail").attrib["callsign"] = callsign
        original.find("detail").find("contact").attrib["callsign"] = callsign

    cot_type = transform.get("cot_type")
    if cot_type:
        original.attrib["type"] = cot_type

    # <usericon iconsetpath="66f14976-4b62-4023-8edb-d8d2ebeaa336/Public Safety Air/CIV_FIXED_ISR.png"/>
    icon = transform.get("icon")
    if icon:
        iconsetpath = f"66f14976-4b62-4023-8edb-d8d2ebeaa336/Public Safety Air/{icon}"
        usericon = ET.Element("usericon")
        usericon.set("iconsetpath", iconsetpath)
        original.append(usericon)
        print(ET.tostring(original))

    return original
