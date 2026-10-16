
import glfw
import numpy as np
from OpenGL.GL import *
import ctypes

# Get user input
print("OPENGL PROGRAM USING VERTEX AND FRAGMENT SHADERS")

vertices = []

for i in range(3):
    print(f"\nEnter coordinates for vertex {i + 1}:")
    x = float(input("X coordinate (-1 to 1): "))
    y = float(input("Y coordinate (-1 to 1): "))

    print("Enter color (values between 0 and 1):")
    r = float(input("Red: "))
    g = float(input("Green: "))
    b = float(input("Blue: "))

    vertices.extend([x, y, 0.0, r, g, b])

vertices = np.array(vertices, dtype=np.float32)

# Initialize GLFW
if not glfw.init():
    raise Exception("GLFW initialization failed")

# Request OpenGL 3.3 Core Profile for macOS
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)

# Create window
window = glfw.create_window(800, 600, "OpenGL User Input", None, None)

if not window:
    glfw.terminate()
    raise Exception("Could not create OpenGL window")

glfw.make_context_current(window)

# Vertex shader
vertex_shader_source = """
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;

out vec3 vertexColor;

void main()
{
    gl_Position = vec4(aPos, 1.0);
    vertexColor = aColor;
}
"""

# Fragment shader
fragment_shader_source = """
#version 330 core
in vec3 vertexColor;
out vec4 FragColor;

void main()
{
    FragColor = vec4(vertexColor, 1.0);
}
"""

# Compile vertex shader
vs = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vs, vertex_shader_source)
glCompileShader(vs)

if not glGetShaderiv(vs, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(vs).decode()
    glfw.terminate()
    raise RuntimeError("Vertex shader error: " + error)

# Compile fragment shader
fs = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fs, fragment_shader_source)
glCompileShader(fs)

if not glGetShaderiv(fs, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(fs).decode()
    glfw.terminate()
    raise RuntimeError("Fragment shader error: " + error)

# Link shaders
program = glCreateProgram()
glAttachShader(program, vs)
glAttachShader(program, fs)
glLinkProgram(program)

if not glGetProgramiv(program, GL_LINK_STATUS):
    error = glGetProgramInfoLog(program).decode()
    glfw.terminate()
    raise RuntimeError("Shader linking error: " + error)

glDeleteShader(vs)
glDeleteShader(fs)

# Create VAO and VBO
vao = glGenVertexArrays(1)
vbo = glGenBuffers(1)

glBindVertexArray(vao)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

# Position attribute
glVertexAttribPointer(
    0, 3, GL_FLOAT, GL_FALSE,
    6 * vertices.itemsize, ctypes.c_void_p(0)
)
glEnableVertexAttribArray(0)

# Color attribute
glVertexAttribPointer(
    1, 3, GL_FLOAT, GL_FALSE,
    6 * vertices.itemsize,
    ctypes.c_void_p(3 * vertices.itemsize)
)
glEnableVertexAttribArray(1)

# Render loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(program)
    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)

# Cleanup
glDeleteVertexArrays(1, [vao])
glDeleteBuffers(1, [vbo])
glDeleteProgram(program)

glfw.terminate()
