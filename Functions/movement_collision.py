def move(entity, tiles, velocity):
    rect_ob = entity.collide_rect

    # X-axis check
    rect_ob.x += int(velocity[0])

    colliders = collide_detect(rect_ob, tiles)

    if len(colliders) == 0:  # No collision
        entity.left_collision = False
        entity.right_collision = False
        entity.top_collision = False
        entity.bottom_collision = False
        entity.has_jumped = True

    elif len(colliders) >= 1:  # Collision
        for tile in colliders:

            if entity.velocity[0] > 0:  # Right collision
                entity.right_collision = True
                rect_ob.right = tile.left
                entity.velocity[0] = 0
                entity.accel[0] = 0

            elif entity.velocity[0] < 0:  # Right collision
                entity.left_collision = True
                rect_ob.left = tile.right
                entity.velocity[0] = 0
                entity.accel[0] = 0

    entity.x = rect_ob.x

    # Y-axis check
    rect_ob.y += velocity[1]
    colliders = collide_detect(rect_ob, tiles)

    if len(colliders) == 0:  # No collision
        entity.left_collision = False
        entity.right_collision = False
        entity.top_collision = False
        entity.bottom_collision = False
        entity.has_jumped = True

    elif len(colliders) >= 1:  # Collision
        for tile in colliders:
            if entity.velocity[1] > 0:  # Bottom collision
                entity.bottom_collision = True
                entity.has_jumped = False
                rect_ob.bottom = tile.top
                entity.velocity[1] = 0
                entity.accel[1] = 0

            elif entity.velocity[1] < 0:  # Top collision
                entity.top_collision = True
                rect_ob.top = tile.bottom
                entity.velocity[1] = 0
                entity.accel[1] = 0
    entity.y = rect_ob.y

    return rect_ob


def collide_detect(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile.collide_rect):
            collisions.append(tile.collide_rect)
    return collisions
