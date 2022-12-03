defmodule Day1 do
  def top_n(path, count) do
    chunk_func = fn
      "\n", acc -> {:cont, acc, 0}
      element, acc -> {:cont, acc + elem(Integer.parse(element),0)}
    end

    after_func = fn
      0 -> {:cont, 0}
      count -> {:cont, count, 0}
    end

    File.stream!(path)
      |> Stream.chunk_while(0, chunk_func, after_func)
      |> Enum.sort_by(fn x -> -x end)
      |> Enum.take(count)
      |> Enum.sum()
      |> IO.puts()
  end
end

Day1.top_n("input", 1)
Day1.top_n("input", 3)