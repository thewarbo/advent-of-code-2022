defmodule Day2 do

    def easy_points(line) do
        <<opp, _, player, 10>> = line
        (player - 87) + 3 * rem(player - opp - 1, 3)
    end

    def hard_points(line) do
        <<opp, _, result, 10>> = line
        3 * (result - 88) + rem(opp + result - 1, 3) + 1
    end

    def answer(input, method) do
        File.stream!(input)
          |> Enum.map(method)
          |> Enum.reduce(&+/2)
    end

end

IO.puts(Day2.answer("test-input", &Day2.easy_points/1))
IO.puts(Day2.answer("test-input", &Day2.hard_points/1))
IO.puts(Day2.answer("input", &Day2.easy_points/1))
IO.puts(Day2.answer("input", &Day2.hard_points/1))