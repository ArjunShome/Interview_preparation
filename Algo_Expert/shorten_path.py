def shortenPath(path):
    # Write your code here.
    stack = []
    if len(path) == 1 or len(path.split("/")) == 1:
        return path
    path_has_root = True if path.split("/")[0] == "" else False

    if path_has_root:
        out_str = shortenPathhelper(stack, dir, path, path_has_root)
    else:
        out_str = shortenPathhelper(stack, dir, path,  path_has_root)
    return out_str.replace("//","/")


def shortenPathhelper(stack, dir, path, path_has_root):
    exclude_dir = "." if not path_has_root else ".."
    for dir in path.split("/"):
        if stack:
            if dir == ".." and stack[-1] != '' if path_has_root else "..":
                stack.pop()
            elif dir in [".", '']:
                continue
            else:
                if dir != exclude_dir:
                    stack.append(dir)
        else:
            if dir != exclude_dir:
                stack.append(dir)
        out_str = "/".join(stack)
        if path_has_root and not out_str:
            out_str = "/"
    return out_str.replace("//","/")


# To be optimized in above 

def shortenPath(path):
    # Write your code here.
    stack = []
    if len(path) == 1 or len(path.split("/")) == 1:
        return path
    path_has_root = True if path.split("/")[0] == "" else False
    if path_has_root:
        for dir in path.split("/"):
            if stack:
                if dir == ".." and stack[-1] != '':
                    stack.pop()
                elif dir in [".", '']:
                    continue
                else:
                    if dir != "..":
                        stack.append(dir)
            else:
                if dir != "..":
                    stack.append(dir)
        out_str = "/".join(stack)
        if not out_str:
            out_str = "/"
    else:
        for dir in path.split("/"):
            if stack:
                if dir == ".." and stack[-1] != "..":
                    stack.pop()
                elif dir in [".",""]:
                    continue
                else:
                    stack.append(dir)
            else:
                if dir != ".":
                    stack.append(dir)

        out_str = "/".join(stack)
    return out_str.replace("//","/")



if __name__ == '__main__':
    path = "/foo/../test/../test/../foo//bar/./baz"
    path = "../../foo/bar/baz"
    # path = "/../../foo/../../bar/baz"
    # path = "/"
    # path = "./.."
    # path = "/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../.."
    print(shortenPath(path=path))