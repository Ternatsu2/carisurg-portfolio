# Accessibility Considerations One-Pager

**Interface:** Nurse-facing emergency-triage queue and alert panel  
**Boundary:** Fictional shadow-mode prototype; the nurse owns the final decision

## Information cannot depend on colour

Every urgency state repeats its meaning through the primary action, tier label,
symbol, border treatment, and queue position. The words-only test is completed
before colour is evaluated. A greyscale display, colour-vision difference, or
degraded monitor must not reverse the intended urgency order.

## Readability in a busy emergency department

- Primary alerts use plain English, active voice, and no more than twelve words.
- The alert action is placed before supporting data and stays within two lines.
- Body text starts at 16 px in the prototype, with 1.4 line spacing and no
  condensed or decorative type.
- Dark text on a light background and alert text/background pairs are selected
  to meet WCAG AA contrast. Glare and low-brightness checks remain in the test
  plan because a numerical contrast ratio does not reproduce the clinical room.
- Abbreviations and model details are kept out of the primary alert. Clinical
  context is grouped below it and can be expanded without crowding the queue.

## Keyboard, zoom, and motion

The reading and action order follows the visible order. Every control must be
reachable by keyboard, keep a visible focus indicator, and have a descriptive
label. At 200% zoom, the alert message, tier, and action must remain visible
without horizontal scrolling. The interface uses no flashing content or
essential animation; reduced-motion settings must not hide status changes.

## Hearing, speech, and workload

Audio can reinforce a validated critical or high alert but cannot carry the
message alone. Medium and low tiers are silent by default to limit alarm
fatigue. Acknowledge and mute actions must keep the visual state and audit log.
The screen presents one primary action at a time, separates imported values
from nurse-entered values, and keeps the manual triage route available.

## Known limits and next checks

This interim prototype has not yet been tested with clinicians or assistive
technology users. Peer testing will cover words-only ranking, greyscale, 200%
zoom, keyboard order, glare simulation, alert recognition, error recovery, and
the confirm/override path. Clinical timing, sound patterns, local terminology,
screen-reader behaviour, and use under real ED workload require later clinical
and accessibility review.

