#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)"
walkthrough="$root/week9/walkthrough"
tmp="$walkthrough/.video-build"
transcript="$walkthrough/transcript.md"
output="$walkthrough/week9-final-walkthrough.mp4"

mkdir -p "$tmp"

awk '/^## Opening/{f=1;next}/^## HCI co-design canvas/{f=0}f' "$transcript" > "$tmp/01.txt"
awk '/^## HCI co-design canvas/{f=1;next}/^## HRI co-design canvas/{f=0}f' "$transcript" > "$tmp/02.txt"
awk '/^## HRI co-design canvas/{f=1;next}/^## HCI mock-up/{f=0}f' "$transcript" > "$tmp/03.txt"
awk '/^## HCI mock-up/{f=1;next}/^## HRI mock-up/{f=0}f' "$transcript" > "$tmp/04.txt"
awk '/^## HRI mock-up/{f=1;next}/^## Deployment requirements/{f=0}f' "$transcript" > "$tmp/05.txt"
awk '/^## Deployment requirements/{f=1;next}/^## Safety and close/{f=0}f' "$transcript" > "$tmp/06.txt"
awk '/^## Safety and close/{f=1;next}f' "$transcript" > "$tmp/07.txt"

images=(
  "$walkthrough/title-card.png"
  "$root/week9/co-design-canvas.png"
  "$root/week9/hri-co-design-canvas.png"
  "$root/week9/mockups/triage-review.png"
  "$root/week9/mockups/hri-intake-assistant.png"
  "$walkthrough/deployment-summary.png"
  "$root/week9/safety-one-pager.png"
)

: > "$tmp/segments.txt"
for index in 0 1 2 3 4 5 6; do
  segment="$(printf '%02d' "$((index + 1))")"
  say -v Samantha -r 178 -f "$tmp/$segment.txt" -o "$tmp/$segment.aiff"
  ffmpeg -loglevel error -y \
    -loop 1 -i "${images[$index]}" \
    -i "$tmp/$segment.aiff" \
    -vf "crop=1600:900:0:0,format=yuv420p" \
    -c:v libx264 -tune stillimage -preset medium -crf 24 \
    -c:a aac -b:a 128k -shortest "$tmp/$segment.mp4"
  printf "file '%s/%s.mp4'\n" "$tmp" "$segment" >> "$tmp/segments.txt"
done

ffmpeg -loglevel error -y -f concat -safe 0 -i "$tmp/segments.txt" -c copy "$output"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$output"
