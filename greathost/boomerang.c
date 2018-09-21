// address: 0x8048790
int main(int argc, char *argv[], char *envp[]) {
    __size32 eax; 		// r24

    puts("\n#########################################################\n### Welcome to the \"wysiNwyg\" challenge!\n###     Your task is to find out the password to be able\n###     to decrypt the password-protected zip and read\n###     the secret flag. Good Luck!!\n#########################################################\n");
    printf("Password: ");
    memset(0x8049d60, 0, 35);
    eax = *0x8049d40;
    fgets(0x8049d60, 35, eax);
    if (eax != 0) {
        strlen(0x8049d60);
        eax = *(unsigned char*)(eax + 0x8049d5f);
        if ((unsigned char) eax == 10) {
            strlen(0x8049d60);
            *(__size8*)(eax + 0x8049d5f) = 0;
        }
        strcmp(0x8049d60, 0x8048a73);
        if (eax != 0) {
            strlen(0x8049d60);
            if (eax != 34) {
                puts("Try again :(");
            }
        } else {
            puts("This is not the solution you are looking for :)");
        }
    }
    return 0;
}

