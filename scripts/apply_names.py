"""Apply a reviewed plan. Preview is the default; --apply enables writes."""
if __package__:
    from .patch_plans import main
else:
    from patch_plans import main

if __name__ == '__main__':
    raise SystemExit(main(('model_name', 'aircraft_name', 'aliases')))
