# TODO: Add more compressions

HEADER_OFFSET = 16384

WEB_MERCATOR_EPSG = 3857

COMPRESSIONS = {
    1: "uncompressed",
    5: "lzw",
    6: "jpeg",
    7: "jpeg",
    8: "deflate",
    50001: "webp"
}

INTERLEAVE = {
    1: "pixel",
    2: "band"
}

# https://github.com/cgohlke/tifffile/blob/master/tifffile/tifffile.py#L7901-L7986
# Map SampleFormat and BitsPerSample tags to numpy dtype
SAMPLE_DTYPES = {
            # UINT
            (1, 1): '?',  # bitmap
            (1, 2): 'B',
            (1, 3): 'B',
            (1, 4): 'B',
            (1, 5): 'B',
            (1, 6): 'B',
            (1, 7): 'B',
            (1, 8): 'B',
            (1, 9): 'H',
            (1, 10): 'H',
            (1, 11): 'H',
            (1, 12): 'H',
            (1, 13): 'H',
            (1, 14): 'H',
            (1, 15): 'H',
            (1, 16): 'H',
            (1, 17): 'I',
            (1, 18): 'I',
            (1, 19): 'I',
            (1, 20): 'I',
            (1, 21): 'I',
            (1, 22): 'I',
            (1, 23): 'I',
            (1, 24): 'I',
            (1, 25): 'I',
            (1, 26): 'I',
            (1, 27): 'I',
            (1, 28): 'I',
            (1, 29): 'I',
            (1, 30): 'I',
            (1, 31): 'I',
            (1, 32): 'I',
            (1, 64): 'Q',
            # VOID : treat as UINT
            (4, 1): '?',  # bitmap
            (4, 2): 'B',
            (4, 3): 'B',
            (4, 4): 'B',
            (4, 5): 'B',
            (4, 6): 'B',
            (4, 7): 'B',
            (4, 8): 'B',
            (4, 9): 'H',
            (4, 10): 'H',
            (4, 11): 'H',
            (4, 12): 'H',
            (4, 13): 'H',
            (4, 14): 'H',
            (4, 15): 'H',
            (4, 16): 'H',
            (4, 17): 'I',
            (4, 18): 'I',
            (4, 19): 'I',
            (4, 20): 'I',
            (4, 21): 'I',
            (4, 22): 'I',
            (4, 23): 'I',
            (4, 24): 'I',
            (4, 25): 'I',
            (4, 26): 'I',
            (4, 27): 'I',
            (4, 28): 'I',
            (4, 29): 'I',
            (4, 30): 'I',
            (4, 31): 'I',
            (4, 32): 'I',
            (4, 64): 'Q',
            # INT
            (2, 8): 'b',
            (2, 16): 'h',
            (2, 32): 'i',
            (2, 64): 'q',
            # IEEEFP : 24 bit not supported by numpy
            (3, 16): 'e',
            # (3, 24): '',  #
            (3, 32): 'f',
            (3, 64): 'd',
            # COMPLEXIEEEFP
            (6, 64): 'F',
            (6, 128): 'D',
            # RGB565
            (1, (5, 6, 5)): 'B',
            # COMPLEXINT : not supported by numpy
        }

# https://github.com/python-pillow/Pillow/blob/master/src/PIL/TiffTags.py
TIFF_TAGS = {
    254: "NewSubfileType",
    255: "SubfileType",
    256: "ImageWidth",
    257: "ImageHeight",
    258: "BitsPerSample",
    259: "Compression",
    262: "PhotometricInterpretation",
    263: "Threshholding",
    264: "CellWidth",
    265: "CellHeight",
    266: "FillOrder",
    269: "DocumentName",
    270: "ImageDescription",
    271: "Make",
    272: "Model",
    273: "StripOffsets",
    274: "Orientation",
    277: "SamplesPerPixel",
    278: "RowsPerStrip",
    279: "StripByteCounts",
    280: "MinSampleValue",
    281: "MaxSampleValue",
    282: "XResolution",
    283: "YResolution",
    284: "PlanarConfiguration",
    285: "PageName",
    286: "XPosition",
    287: "YPosition",
    288: "FreeOffsets",
    289: "FreeByteCounts",
    290: "GrayResponseUnit",
    291: "GrayResponseCurve",
    292: "T4Options",
    293: "T6Options",
    296: "ResolutionUnit",
    297: "PageNumber",
    301: "TransferFunction",
    305: "Software",
    306: "DateTime",
    315: "Artist",
    316: "HostComputer",
    317: "Predictor",
    318: "WhitePoint",
    319: "PrimaryChromaticities",
    320: "ColorMap",
    321: "HalftoneHints",
    322: "TileWidth",
    323: "TileHeight",
    324: "TileOffsets",
    325: "TileByteCounts",
    332: "InkSet",
    333: "InkNames",
    334: "NumberOfInks",
    336: "DotRange",
    337: "TargetPrinter",
    338: "ExtraSamples",
    339: "SampleFormat",
    340: "SMinSampleValue",
    341: "SMaxSampleValue",
    342: "TransferRange",
    347: "JPEGTables",
    512: "JPEGProc",
    513: "JPEGInterchangeFormat",
    514: "JPEGInterchangeFormatLength",
    515: "JPEGRestartInterval",
    517: "JPEGLosslessPredictors",
    518: "JPEGPointTransforms",
    519: "JPEGQTables",
    520: "JPEGDCTables",
    521: "JPEGACTables",
    529: "YCbCrCoefficients",
    530: "YCbCrSubSampling",
    531: "YCbCrPositioning",
    532: "ReferenceBlackWhite",
    700: "XMP",
    33432: "Copyright",
    33723: "IptcNaaInfo",
    34377: "PhotoshopInfo",
    34665: "ExifIFD",
    34675: "ICCProfile",
    34853: "GPSInfoIFD",
    45056: "MPFVersion",
    45057: "NumberOfImages",
    45058: "MPEntry",
    45059: "ImageUIDList",
    45060: "TotalFrames",
    45313: "MPIndividualNum",
    45569: "PanOrientation",
    45570: "PanOverlap_H",
    45571: "PanOverlap_V",
    45572: "BaseViewpointNum",
    45573: "ConvergenceAngle",
    45574: "BaselineLength",
    45575: "VerticalDivergence",
    45576: "AxisDistance_X",
    45577: "AxisDistance_Y",
    45578: "AxisDistance_Z",
    45579: "YawAngle",
    45580: "PitchAngle",
    45581: "RollAngle",
    50741: "MakerNoteSafety",
    50780: "BestQualityScale",
    50838: "ImageJMetaDataByteCounts",
    50839: "ImageJMetaData",
    32932: "Wang Annotation",
    33434: "ExposureTime",
    33437: "FNumber",
    33445: "MD FileTag",
    33446: "MD ScalePixel",
    33447: "MD ColorTable",
    33448: "MD LabName",
    33449: "MD SampleInfo",
    33450: "MD PrepDate",
    33451: "MD PrepTime",
    33452: "MD FileUnits",
    33550: "ModelPixelScaleTag",
    33918: "INGR Packet Data Tag",
    33919: "INGR Flag Registers",
    33920: "IrasB Transformation Matrix",
    33922: "ModelTiepointTag",
    34264: "ModelTransformationTag",
    34735: "GeoKeyDirectoryTag",
    34736: "GeoDoubleParamsTag",
    34737: "GeoAsciiParamsTag",
    34850: "ExposureProgram",
    34852: "SpectralSensitivity",
    34855: "ISOSpeedRatings",
    34856: "OECF",
    34864: "SensitivityType",
    34865: "StandardOutputSensitivity",
    34866: "RecommendedExposureIndex",
    34867: "ISOSpeed",
    34868: "ISOSpeedLatitudeyyy",
    34869: "ISOSpeedLatitudezzz",
    34908: "HylaFAX FaxRecvParams",
    34909: "HylaFAX FaxSubAddress",
    34910: "HylaFAX FaxRecvTime",
    36864: "ExifVersion",
    36867: "DateTimeOriginal",
    36868: "DateTImeDigitized",
    37121: "ComponentsConfiguration",
    37122: "CompressedBitsPerPixel",
    37724: "ImageSourceData",
    37377: "ShutterSpeedValue",
    37378: "ApertureValue",
    37379: "BrightnessValue",
    37380: "ExposureBiasValue",
    37381: "MaxApertureValue",
    37382: "SubjectDistance",
    37383: "MeteringMode",
    37384: "LightSource",
    37385: "Flash",
    37386: "FocalLength",
    37396: "SubjectArea",
    37500: "MakerNote",
    37510: "UserComment",
    37520: "SubSec",
    37521: "SubSecTimeOriginal",
    37522: "SubsecTimeDigitized",
    40960: "FlashPixVersion",
    40961: "ColorSpace",
    40962: "PixelXDimension",
    40963: "PixelYDimension",
    40964: "RelatedSoundFile",
    40965: "InteroperabilityIFD",
    41483: "FlashEnergy",
    41484: "SpatialFrequencyResponse",
    41486: "FocalPlaneXResolution",
    41487: "FocalPlaneYResolution",
    41488: "FocalPlaneResolutionUnit",
    41492: "SubjectLocation",
    41493: "ExposureIndex",
    41495: "SensingMethod",
    41728: "FileSource",
    41729: "SceneType",
    41730: "CFAPattern",
    41985: "CustomRendered",
    41986: "ExposureMode",
    41987: "WhiteBalance",
    41988: "DigitalZoomRatio",
    41989: "FocalLengthIn35mmFilm",
    41990: "SceneCaptureType",
    41991: "GainControl",
    41992: "Contrast",
    41993: "Saturation",
    41994: "Sharpness",
    41995: "DeviceSettingDescription",
    41996: "SubjectDistanceRange",
    42016: "ImageUniqueID",
    42032: "CameraOwnerName",
    42033: "BodySerialNumber",
    42034: "LensSpecification",
    42035: "LensMake",
    42036: "LensModel",
    42037: "LensSerialNumber",
    42112: "GDAL_METADATA",
    42113: "GDAL_NODATA",
    42240: "Gamma",
    50215: "Oce Scanjob Description",
    50216: "Oce Application Selector",
    50217: "Oce Identification Number",
    50218: "Oce ImageLogic Characteristics",
    50706: "DNGVersion",
    50707: "DNGBackwardVersion",
    50708: "UniqueCameraModel",
    50709: "LocalizedCameraModel",
    50710: "CFAPlaneColor",
    50711: "CFALayout",
    50712: "LinearizationTable",
    50713: "BlackLevelRepeatDim",
    50714: "BlackLevel",
    50715: "BlackLevelDeltaH",
    50716: "BlackLevelDeltaV",
    50717: "WhiteLevel",
    50718: "DefaultScale",
    50719: "DefaultCropOrigin",
    50720: "DefaultCropSize",
    50721: "ColorMatrix1",
    50722: "ColorMatrix2",
    50723: "CameraCalibration1",
    50724: "CameraCalibration2",
    50725: "ReductionMatrix1",
    50726: "ReductionMatrix2",
    50727: "AnalogBalance",
    50728: "AsShotNeutral",
    50729: "AsShotWhiteXY",
    50730: "BaselineExposure",
    50731: "BaselineNoise",
    50732: "BaselineSharpness",
    50733: "BayerGreenSplit",
    50734: "LinearResponseLimit",
    50735: "CameraSerialNumber",
    50736: "LensInfo",
    50737: "ChromaBlurRadius",
    50738: "AntiAliasStrength",
    50740: "DNGPrivateData",
    50778: "CalibrationIlluminant1",
    50779: "CalibrationIlluminant2",
    50784: "Alias Layer Metadata",
}
