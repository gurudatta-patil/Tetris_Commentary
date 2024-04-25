import ytdown
import requester
import info_extracter
import tts
if __name__=="__main__":
    ytdown.downloader("https://www.youtube.com/watch?v=L_UPHsGR6fM")
    info_extracter.extract_info_from_frames()
    text=requester.requester()
    # text="Joseph is showing his Tetris prowess with a lead over JoNaS. Scores are close, with both players strategizing at level 18. Joseph excels with an 85% Tetris rate, while JoNaS employs a burning strategy. The high-stakes match intensifies as they battle for victory.Joseph's lead grows as he displays skill and precision. JoNaS remains determined, focusing on strategy. The tension rises in this thrilling Tetris showdown. Strategies clash as blocks fall rapidly. Both players aim for victory in this neck-to-neck battle.The intense Tetris battle continues, with Joseph's calculated moves keeping him ahead. JoNaS strategizes in an attempt to catch up. Precision and strategy merge as the players navigate the Tetris grid. The competition remains fierce as Joseph’s lead maintains the pressure.Joseph's dominance is on display as JoNaS strives to close the gap. Both players showcase their skills with differing strategies. Joseph's well-rounded gameplay stands out, while JoNaS focuses on a strategic approach. The tension mounts as the Tetris battle intensifies.The Tetris battle reaches a pivotal moment as Joseph takes the lead. JoNaS aims to shift the momentum with strategic moves. The competition remains fierce as both players navigate the Tetris grid. Precision and strategy define each player's approach in this gripping match."
    tts.add_ttl_to_video("./tmp/output.mp4",text, './output_with_commentary.mp4')