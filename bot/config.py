#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("a9e62ec83fe3c22379e3e19195c8b3f6", cast=int)
    API_HASH = config("3281305")
    BOT_TOKEN = config("1929972601:AAE9UKpipafRDDA-tgl1HmmL6zQpjw6a7cI")
    DEV = 1322549723
    OWNER = config("1666551439")
    FFMPEG = config(
        "ffmpeg -i '''{}'''  -filter_complex 'drawtext=fontfile=njnaruto.ttf:fontsize=25:fontcolor=white:bordercolor=black@0.50:x=w-tw-10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text='Animes-Encoded'':enable='between(t,0,15)':alpha='if(lt(t,14)\\,1\\,if(lt(t\\,15)\\,(1-(t-14))/1\\,0))', drawtext=fontfile=njnaruto.ttf:text='\\|\\| Download From The Original Place https\\://t.me/Animes_Encoded \\|\\| And For Animes Request https\\://t.me/Anime_Hub_Group':bordercolor=black@0.50:borderw=5:fontcolor=white:fontsize=30:x=w-((2*w-200)*(t-615)/60):y=lh+0.5:enable='between(t, 615,680)':alpha='if(lt(t,679)\\,1\\,if(lt(t\\,680)\\,(1-(t-679))/1\\,0))'[out1]'' -metadata:s:a:0 title=''[Telegram: @Animes_Encoded]'' -metadata:s:a:1 title=''[Telegram: @Animes_Encoded]'' -metadata:s:s:0 title=''[Telegram: @Animes_Encoded]~English'' -metadata:s:s:1 title=''[Telegram: @Animes_Encoded]~English'' -map [out1] -map 0:a? -map 0:s? -map 0:t? -metadata title='Animes_Encoded - 480p'' -c:v libx265 -pix_fmt yuv420p -preset medium -s 846x480 -crf 32.8 -c:a libfdk_aac -profile:a aac_he_v2  -ac 2 -vbr 2 -c:s copy -movflags +faststart '''{}'''  -y",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config("https://telegra.ph/file/269d7d7b5f11635d4c8a0.jpg")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
