import cv2
# import pytesseract
# from tesseract import image_to_string
import pandas as pd
import os
import easyocr #pip install easyocr
import blockdetector

# Path to the folder containing frames
def extract_info_from_frames():
    frames_folder = './frames'
    tmp_dir = './tmp'
    # Define the regions of interest (ROIs) on the screen
    player1_name_roi = (420, 604, 596, 638)  # (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    player2_name_roi = (672, 604, 846, 638)  # (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    player1_score_roi = (424, 24, 604, 100)  # (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    player2_score_roi = (680, 24, 866, 100)  # (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    player1_line_roi = (416, 146, 496, 170)  # Needs to be fixed # fixed with easyOCR
    player2_line_roi = (672, 146, 754, 170)  # Needs to be fixed # fixed with easyOCR
    player1_lvl_roi = (348, 388, 394, 434) # Needs to be fixed # fixed with easyOCR
    player2_lvl_roi = (888, 388, 932, 436) # Needs to be fixed # fixed with easyOCR
    player1_trt_roi = (326, 460, 392, 498) 
    player2_brn_roi = (894, 454, 952, 502)
    player1_block = (413, 193, 608, 589) 
    player2_block = (671, 193, 866, 589)
    # Initialize an empty DataFrame to store the extracted information
    data = []

    # Loop through all the frame files in the frames folder
    for filename in os.listdir(frames_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Get the full path of the frame file
            frame_path = os.path.join(frames_folder, filename)

            # Read the frame
            frame = cv2.imread(frame_path)

            # Extract ROIs
            player1_name_roi_img = frame[player1_name_roi[1]:player1_name_roi[3], player1_name_roi[0]:player1_name_roi[2]]
            player2_name_roi_img = frame[player2_name_roi[1]:player2_name_roi[3], player2_name_roi[0]:player2_name_roi[2]]
            player1_score_roi_img = frame[player1_score_roi[1]:player1_score_roi[3], player1_score_roi[0]:player1_score_roi[2]]
            player2_score_roi_img = frame[player2_score_roi[1]:player2_score_roi[3], player2_score_roi[0]:player2_score_roi[2]]
            player1_line_roi_img = frame[player1_line_roi[1]:player1_line_roi[3], player1_line_roi[0]:player1_line_roi[2]]
            player2_line_roi_img = frame[player2_line_roi[1]:player2_line_roi[3], player2_line_roi[0]:player2_line_roi[2]]
            player1_lvl_roi_img = frame[player1_lvl_roi[1]:player1_lvl_roi[3], player1_lvl_roi[0]:player1_lvl_roi[2]]
            player2_lvl_roi_img = frame[player2_lvl_roi[1]:player2_lvl_roi[3], player2_lvl_roi[0]:player2_lvl_roi[2]]
            player1_trt_roi_img = frame[player1_trt_roi[1]:player1_trt_roi[3], player1_trt_roi[0]:player1_trt_roi[2]]
            player2_brn_roi_img = frame[player2_brn_roi[1]:player2_brn_roi[3], player2_brn_roi[0]:player2_brn_roi[2]]
            player1_block_roi_img = frame[player1_block[1]:player1_block[3], player1_block[0]:player1_block[2]]
            player2_block_roi_img = frame[player2_block[1]:player2_block[3], player2_block[0]:player2_block[2]] 
            


            # Save ROIs as separate images
            cv2.imwrite(os.path.join(tmp_dir, 'player1_name_roi.jpg'), player1_name_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player2_name_roi.jpg'), player2_name_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player1_score_roi.jpg'), player1_score_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player2_score_roi.jpg'), player2_score_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player1_line_roi.jpg'), player1_line_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player2_line_roi.jpg'), player2_line_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player1_lvl_roi.jpg'), player1_lvl_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player2_lvl_roi.jpg'), player2_lvl_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player1_trt_roi.jpg'), player1_trt_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player2_brn_roi.jpg'), player2_brn_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player1_block_roi.jpg'), player1_block_roi_img)
            cv2.imwrite(os.path.join(tmp_dir, 'player2_block_roi.jpg'), player2_block_roi_img)

            # Perform OCR on ROIs # Pytesseract
            # player1_name = pytesseract.image_to_string(player1_name_roi_img)
            # player2_name = pytesseract.image_to_string(player2_name_roi_img)
            # player1_score = pytesseract.image_to_string(player1_score_roi_img)
            # player2_score = pytesseract.image_to_string(player2_score_roi_img)
            # player1_line = pytesseract.image_to_string(player1_line_roi_img)
            # player2_line = pytesseract.image_to_string(player2_line_roi_img)
            # player1_lvl = pytesseract.image_to_string(player1_lvl_roi_img)
            # player2_lvl = pytesseract.image_to_string(player2_lvl_roi_img)
            # player1_trt = pytesseract.image_to_string(player1_trt_roi_img)
            # player2_brn = pytesseract.image_to_string(player2_brn_roi_img)

            reader = easyocr.Reader(['en'])

            # Perform OCR on ROIs
            # Perform OCR on ROIs
            try:
                player1_name = reader.readtext(player1_name_roi_img)[0][1]
            except IndexError:
                player1_name = ''
            try:
                player2_name = reader.readtext(player2_name_roi_img)[0][1]
            except IndexError:
                player2_name = ''
            try:
                player1_score = reader.readtext(player1_score_roi_img)[1][1]
            except IndexError:
                player1_score = ''
            try:
                player2_score = reader.readtext(player2_score_roi_img)[1][1]
            except IndexError:
                player2_score = ''
            try:
                player1_line = reader.readtext(player1_line_roi_img)[0][1]
            except IndexError:
                player1_line = ''
            try:
                player2_line = reader.readtext(player2_line_roi_img)[0][1]
            except IndexError:
                player2_line = ''
            try:
                player1_lvl = reader.readtext(player1_lvl_roi_img)[1][1]
            except IndexError:
                player1_lvl = ''
            try:
                player2_lvl = reader.readtext(player2_lvl_roi_img)[1][1]
            except IndexError:
                player2_lvl = ''
            try:
                player1_trt = reader.readtext(player1_trt_roi_img)[1][1]
            except IndexError:
                player1_trt = ''
            try:
                player2_brn = reader.readtext(player2_brn_roi_img)[1][1]
            except IndexError:
                player2_brn = ''
            try:
                player1_block_out = blockdetector.detect_blocks(player1_block_roi_img)
            except IndexError:
                player1_block= ''  
            try:
                player2_block_out = blockdetector.detect_blocks(player2_block_roi_img)
            except IndexError:
                player2_block= ''

            # Append the extracted information to the DataFrame
            data.append({
                'Frame': filename,
                'Player 1 Name': player1_name,
                'Player 2 Name': player2_name,
                'Player 1 Score': player1_score,
                'Player 2 Score': player2_score,
                'Player 1 Line': player1_line,
                'Player 2 Line': player2_line,
                'Player 1 Lvl': player1_lvl,
                'Player 2 Lvl': player2_lvl,
                'Player 1 TRT': player1_trt,
                'Player 2 BRN': player2_brn,
                'Player 1 block': player1_block_out,
                'Player 2 block': player2_block_out,
            })

            # Print OCR read values
            print(f'Frame: {filename}')
            print(f'Player 1 Name: {player1_name}')
            print(f'Player 2 Name: {player2_name}')
            print(f'Player 1 Score: {player1_score}')
            print(f'Player 2 Score: {player2_score}')
            print(f'Player 1 Line: {player1_line}')
            print(f'Player 2 Line: {player2_line}')
            print(f'Player 1 Lvl: {player1_lvl}')
            print(f'Player 2 Lvl: {player2_lvl}')
            print(f'Player 1 TRT: {player1_trt}')
            print(f'Player 2 BRN: {player2_brn}')
            print(f'Player 1 block: {player1_block_out}')
            print(f'Player 2 block: {player2_block_out}')
            print('---')

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)
    df = df.sort_values('Frame')

    # Save the DataFrame to a CSV file
    df.to_csv('extracted_data.csv', index=False)
