   #!/bin/bash
   echo "setup.sh started" >> setup.log
   sudo apt-get update -y >> setup.log 2>&1
   sudo apt-get install -y tesseract-ocr tesseract-ocr-eng >> setup.log 2>&1
   echo "setup.sh finished" >> setup.log