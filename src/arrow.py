import pygame
from enums import Code

# https://www.reddit.com/r/pygame/comments/v3ofs9/draw_arrow_function/
def drawArrow(
        surface: pygame.Surface,
        start: pygame.Vector2,
        end: pygame.Vector2,
        color: pygame.Color,
        body_width: int = 2,
        head_width: int = 4,
        head_height: int = 2,
    ):
    """Draw an arrow between start and end with the arrow head at the end.

    Args:
        surface (pygame.Surface): The surface to draw on
        start (pygame.Vector2): Start position
        end (pygame.Vector2): End position
        color (pygame.Color): Color of the arrow
        body_width (int, optional): Defaults to 2.
        head_width (int, optional): Defaults to 4.
        head_height (float, optional): Defaults to 2.
    """
    arrow = start - end
    angle = arrow.angle_to(pygame.Vector2(0, -1))
    body_length = arrow.length() - head_height

    # Create the triangle head around the origin
    head_verts = [
        pygame.Vector2(0, head_height / 2),  # Center
        pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
        pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
    ]
    # Rotate and translate the head into place
    translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)
    for i in range(len(head_verts)):
        head_verts[i].rotate_ip(-angle)
        head_verts[i] += translation
        head_verts[i] += start

    pygame.draw.polygon(surface, color, head_verts)

    # Stop weird shapes when the arrow is shorter than arrow head
    if arrow.length() >= head_height:
        # Calculate the body rect, rotate and translate into place
        body_verts = [
            pygame.Vector2(-body_width / 2, body_length / 2),  # Topleft
            pygame.Vector2(body_width / 2, body_length / 2),  # Topright
            pygame.Vector2(body_width / 2, -body_length / 2),  # Bottomright
            pygame.Vector2(-body_width / 2, -body_length / 2),  # Bottomleft
        ]
        translation = pygame.Vector2(0, body_length / 2).rotate(-angle)
        for i in range(len(body_verts)):
            body_verts[i].rotate_ip(-angle)
            body_verts[i] += translation
            body_verts[i] += start

        pygame.draw.polygon(surface, color, body_verts)


def drawKey(screen, code : Code, coordinate, color):
    length = 25
    if code == Code.UP:
        start = pygame.Vector2(coordinate[0], coordinate[1] + length // 2)
        end = pygame.Vector2(coordinate[0], coordinate[1] - length // 2)
    if code == Code.LEFT:
        start = pygame.Vector2(coordinate[0] + length // 2, coordinate[1])
        end = pygame.Vector2(coordinate[0] - length // 2, coordinate[1])
    if code == Code.DOWN:
        start = pygame.Vector2(coordinate[0], coordinate[1] - length // 2)
        end = pygame.Vector2(coordinate[0], coordinate[1] + length // 2)
    if code == Code.RIGHT:
        start = pygame.Vector2(coordinate[0] - length // 2, coordinate[1])
        end = pygame.Vector2(coordinate[0] + length // 2, coordinate[1])
    
    drawArrow(screen, start, end, color, 12, 20, 12)