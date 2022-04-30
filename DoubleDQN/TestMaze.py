from MazeEnv import Maze
import unittest
import numpy as np
import random

class TestMaze(unittest.TestCase):
  def setUp(self):
    random.seed(1)
    self.env = Maze(5)
    self.env.reset()
    self.env.print()

  def test_rand_states(self):
    state0 = self.env.get_state()
    self.assertEqual(len(np.argwhere(state0 == Maze.ROB_SYM)), 1)
    self.assertEqual(len(np.argwhere(state0 == Maze.DEST_SYM)), 1)
    for _ in range(5):
      state = self.env.rand_state()
      self.assertEqual(len(np.argwhere(state == Maze.ROB_SYM)), 1)
      self.assertEqual(len(np.argwhere(state == Maze.DEST_SYM)), 1)

  def test_place_rob(self):
    loc = np.array([1, 2])
    r = self.env.place_rob(loc)
    self.assertEqual(r, Maze.FAIL_REWARD)

    loc = np.array([4, 4])
    r = self.env.place_rob(loc)
    self.assertEqual(r, Maze.WIN_REWARD)

  def test_action(self):
    loc = np.array([1, 0])
    r = self.env.place_rob(loc)
    self.assertEqual(r, Maze.NEU_REWARD)
    action = 1
    next_state, reward, done = self.env.action(action)
    print("next state = \n", next_state.reshape(5,5))
    self.assertEqual(reward, Maze.NEU_REWARD)
    self.assertFalse(done)
    action = 1
    next_state, reward, done = self.env.action(action)
    self.assertEqual(reward, Maze.FAIL_REWARD)
    self.assertTrue(done)
    action = 2
    next_state, reward, done = self.env.action(action)
    print("next state = \n", next_state.reshape(5,5))
    self.assertEqual(reward, Maze.NEU_REWARD)
    self.assertFalse(done)


  def test_action3(self):
    action = 3
    next_state, reward, done = self.env.action(action)
    self.assertEqual(reward, Maze.FAIL_REWARD)
    self.assertTrue(done)